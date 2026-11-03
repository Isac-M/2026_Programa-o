import streamlit as st
from service import Service
import time

class PerfilClienteUI:
    def main():
        st.header("Meus Dados")
        try:
            op = Service.cliente_listar_id(st.session_state["usuario_id"])
            if op is None:
                st.error("Cliente não encontrado.")
                return

            nome = st.text_input("Informe o novo nome", op.get_nome())
            email = st.text_input("Informe o novo e-mail", op.get_email())
            fone = st.text_input("Informe o novo fone", op.get_fone())
            senha = st.text_input("Informe a nova senha", op.get_senha(), type="password")

            if st.button("Atualizar"):
                try:
                    id = op.get_id()
                    Service.cliente_atualizar(id, nome, email, fone, senha)
                    st.success("Cliente atualizado com sucesso")
                    time.sleep(2)
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro ao atualizar perfil: {e}")
        except Exception as e:
            st.error(f"Erro ao carregar dados do perfil: {e}")