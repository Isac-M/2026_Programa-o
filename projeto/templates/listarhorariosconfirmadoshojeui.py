import streamlit as st
import datetime 
from views import view

class ListarHorariosConfirmadosHojeUI:

    @staticmethod
    def main():
        st.harder("Horários confirmados hoje")
        horarios = view.horario_listar_confirmados_hoje()

        if len(horarios) == 0:
            st.info("Nenhum horário confirmado para hoje")
        else:
            tabela = []
            for h in horarios:
                data_hora = h.get_data().strftime("%d/%m/%y %h:%m")

                tabela.append({
                    "id":
                    h.get_id(),
                    "data/hora":
                    data_hora,
                    "Cliente":
                    h.get_cliente().get_nome()
                    if h.get_cliente() else "",
                    "Serviço":
                    h.get_servico().get_descricao()
                    if h.get_servico() else "",
                    "Profissional":
                    h.get_profissional().get_nome()
                    if h.get_profissional() else "",
                })

                st.dataframe(tabela, use_container_width=True)