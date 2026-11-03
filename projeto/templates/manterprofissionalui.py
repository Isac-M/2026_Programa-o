import streamlit as st
import pandas as pd
import time
from service import Service

class ManterProfissionalUI:
    @staticmethod
    def main():
        st.header("Cadastro de Profissionais")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterProfissionalUI.listar()
        with tab2: ManterProfissionalUI.inserir()
        with tab3: ManterProfissionalUI.atualizar()
        with tab4: ManterProfissionalUI.excluir()

    @staticmethod
    def listar():
        try:
            profissionais = Service.profissional_listar()
            if len(profissionais) == 0:
                st.write("Nenhum profissional cadastrado")
            else:
                list_dic = [obj.to_dict() for obj in profissionais]
                df = pd.DataFrame(list_dic)
                st.dataframe(df)
        except Exception as e:
            st.error(f"Erro ao listar profissionais: {e}")

    @staticmethod
    def inserir():
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        especialidade = st.text_input("Informe a especialidade")
        senha = st.text_input("Informe a senha", type="password")
        
        if st.button("Inserir"):
            try:
                Service.profissional_inserir(nome, email, especialidade, senha)
                st.success("Profissional inserido com sucesso")
                time.sleep(2)
                st.rerun()
            except Exception as e:
                st.error(f"Erro ao inserir profissional: {e}")

    @staticmethod
    def atualizar():
        try:
            profissionais = Service.profissional_listar()
        except Exception as e:
            st.error(f"Erro ao carregar profissionais: {e}")
            return

        if len(profissionais) == 0:
            st.write("Nenhum profissional cadastrado")
        else:
            op = st.selectbox("Atualização de Profissionais", profissionais)
            nome = st.text_input("Informe o novo nome", op.get_nome())
            email = st.text_input("Informe o novo email", op.get_email())
            especialidade = st.text_input("Informe a nova especialidade", op.get_especialidade())
            senha = st.text_input("Nova senha", op.get_senha(), type="password")

            if st.button("Atualizar"):
                try:
                    id = op.get_id()
                    Service.profissional_atualizar(id, nome, email, especialidade, senha)
                    st.success("Profissional atualizado com sucesso")
                    time.sleep(2)
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro ao atualizar profissional: {e}")

    @staticmethod
    def excluir():
        try:
            profissionais = Service.profissional_listar()
        except Exception as e:
            st.error(f"Erro ao carregar profissionais: {e}")
            return

        if len(profissionais) == 0:
            st.write("Nenhum profissional cadastrado")
        else:
            op = st.selectbox("Exclusão de Profissionais", profissionais)
            if st.button("Excluir"):
                try:
                    id = op.get_id()
                    Service.profissional_excluir(id)
                    st.success("Profissional excluído com sucesso")
                    time.sleep(2)
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro ao excluir profissional: {e}")