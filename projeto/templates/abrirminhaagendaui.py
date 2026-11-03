import streamlit as st
from service import Service
from datetime import datetime
import time

class AbrirMinhaAgendaUI:
    def main():
        st.header("Abrir Minha Agenda")
        data = st.text_input("Informe a data no formato dd/mm/aaaa", datetime.now().strftime("%d/%m/%Y"))
        horario_inicio = st.text_input("Informe o horário inicial no formato HH:MM")
        horario_fim = st.text_input("Informe o horário final no formato HH:MM")
        intervalo = st.text_input("Informe o intervalo entre os horários (min)")
        
        if st.button("Abrir Agenda"):
            try:
                if not data or not horario_inicio or not horario_fim or not intervalo:
                    st.error("Por favor, preencha todos os campos.")
                    return

                try:
                    intervalo_int = int(intervalo)
                    if intervalo_int <= 0:
                        st.error("O intervalo deve ser um número inteiro maior que zero.")
                        return
                except ValueError:
                    st.error("O intervalo deve ser um número inteiro válido (ex: 30, 60).")
                    return

                Service.horario_abrir_minha_agenda(
                    data, 
                    horario_inicio, 
                    horario_fim, 
                    intervalo_int, 
                    st.session_state["usuario_id"]
                )
                
                st.success("Horários inseridos com sucesso")
                time.sleep(2)
                st.rerun()

            except ValueError as e:
                st.error(f"Erro de formato nos dados fornecidos: {e}")
            except KeyError:
                st.error("Sessão expirada ou usuário não identificado. Faça login novamente.")
            except Exception as e:
                st.error(f"Erro ao abrir agenda: {e}")