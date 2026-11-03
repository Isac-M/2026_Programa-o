import streamlit as st
from views import view

class ListarAgendaProfissionalUI:

    @staticmethod
    def main():
        st.harder("Agenda profissional")
        profissionais = view.profissional_listar()

        if len(profissionais) == 0:
            st.info("Nenhum profissional cadastrado")
        else:
            profissional_selecionado = st.selectbox(
                "selecione o profissional"
                options = profissionais,
            )

            if profissional_selecionado:
                horarios = view.horario_listar_profissional(
                    profissional_selecionado.get_id()
                )

                if len(horarios) == 0:
                    st.info(
                        f"Nenhum horário encontrado na agenda de {profissional_selecionado.get_nome()}."
                    )
                else:
                    tabela = []
                    for h in horarios:
                        data_hora = h.get_data().strftime("%d/%m/%y %h:%m")

                        tabela.append({
                            "id"
                            h.get_id(),
                            "data/hora":
                            data_hora,
                            "Cliente":
                            h.get_cliente().get_nome()
                            if h.get_cliente() else "",
                            "Serviço":
                            h.get_servico().get_descricao()
                            if h.get_servico() else "",
                        })

                        st.dataframe(tabela, use_container_width=True)