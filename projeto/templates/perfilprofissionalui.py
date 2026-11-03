import streamlit as st
import time
from service import Service

class PerfilProfissionalUI:
    @staticmethod
    def main():
        st.header("Meus Dados")
        
        try:
            op = Service.profissional_listar_id(st.session_state["usuario_id"])
        except Exception as e:
            st.error(f"Erro ao carregar os dados do perfil: {e}")
            return

        if op is None:
            st.warning("Profissional não encontrado.")
            return

        nome = st.text_input("Informe o novo nome", op.get_nome())
        email = st.text_input("Informe o novo e-mail", op.get_email())
        especialidade = st.text_input("Informe a nova especialidade", op.get_especialidade())
        senha = st.text_input("Informe a nova senha", op.get_senha(), type="password")

        if st.button("Atualizar"):
            try:
                id = op.get_id()
                Service.profissional_atualizar(id, nome, email, especialidade, senha)
                st.success("Profissional atualizado com sucesso")
                time.sleep(2)
                st.rerun()
            except Exception as e:
                st.error(f"Erro ao atualizar o perfil: {e}")