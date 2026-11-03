class Servico:
    __clientes = []
    __profissionais = []
    __horarios = []

    @classmethod
    def cliente_inserir(cls, cliente):
        if cliente.get_email() == "admin":
            raise ValueError("O e-mail 'admin' é reservado para o administrador")
        
        for c in cls.__clientes:
            if c.get_email() == cliente.get_email():
                raise ValueError("E-mail já cadastrado para outro cliente")
                
        for p in cls.__profissionais:
            if p.get_email() == cliente.get_email():
                raise ValueError("E-mail já cadastrado para um profissional")
        
        cls.__clientes.append(cliente)

    @classmethod
    def cliente_atualizar(cls, cliente):
        if cliente.get_email() == "admin":
            raise ValueError("O e-mail 'admin' é reservado para o administrador")
        
        for c in cls.__clientes:
            if c.get_id() != cliente.get_id() and c.get_email() == cliente.get_email():
                raise ValueError("E-mail já utilizado por outro cliente")
                
        for p in cls.__profissionais:
            if p.get_email() == cliente.get_email():
                raise ValueError("E-mail já utilizado por um profissional")

        for i, c in enumerate(cls.__clientes):
            if c.get_id() == cliente.get_id():
                cls.__clientes[i] = cliente
                break

    @classmethod
    def cliente_excluir(cls, id_cliente):
        for horario in cls.__horarios:
            if horario.get_id_cliente() == id_cliente:
                raise ValueError("Não é possível excluir um cliente com horário agendado")

        cls.__clientes = [c for c in cls.__clientes if c.get_id() != id_cliente]

    @classmethod
    def profissional_inserir(cls, profissional):
        if profissional.get_email() == "admin":
            raise ValueError("O e-mail 'admin' é reservado para o administrador")

        for p in cls.__profissionais:
            if p.get_email() == profissional.get_email():
                raise ValueError("E-mail já cadastrado para outro profissional")

        for c in cls.__clientes:
            if c.get_email() == profissional.get_email():
                raise ValueError("E-mail já cadastrado para um cliente")

        cls.__profissionais.append(profissional)

    @classmethod
    def profissional_atualizar(cls, profissional):
        if profissional.get_email() == "admin":
            raise ValueError("O e-mail 'admin' é reservado para o administrador")

        for p in cls.__profissionais:
            if p.get_id() != profissional.get_id() and p.get_email() == profissional.get_email():
                raise ValueError("E-mail já utilizado por outro profissional")

        for c in cls.__clientes:
            if c.get_email() == profissional.get_email():
                raise ValueError("E-mail já utilizado por um cliente")

        for i, p in enumerate(cls.__profissionais):
            if p.get_id() == profissional.get_id():
                cls.__profissionais[i] = profissional
                break

    @classmethod
    def profissional_excluir(cls, id_profissional):
        for horario in cls.__horarios:
            if horario.get_id_profissional() == id_profissional:
                raise ValueError("Não é possível excluir um profissional que tenha cadastrado um horário")

        cls.__profissionais = [p for p in cls.__profissionais if p.get_id() != id_profissional]

    @classmethod
    def horario_inserir(cls, horario):
        for h in cls.__horarios:
            if h.get_id_profissional() == horario.get_id_profissional() and h.get_data() == horario.get_data():
                raise ValueError("Já existe um horário para este profissional nessa mesma data e hora")

        cls.__horarios.append(horario)

    @classmethod
    def horario_atualizar(cls, horario):
        for h in cls.__horarios:
            if h.get_id() != horario.get_id() and h.get_id_profissional() == horario.get_id_profissional() and h.get_data() == horario.get_data():
                raise ValueError("Já existe outro horário para este profissional nessa mesma data e hora")

        for i, h in enumerate(cls.__horarios):
            if h.get_id() == horario.get_id():
                cls.__horarios[i] = horario
                break

    @classmethod
    def horario_excluir(cls, id_horario):
        for h in cls.__horarios:
            if h.get_id() == id_horario:
                if h.get_confirmado() or h.get_id_cliente() != 0:
                    raise ValueError("Não é possível excluir um horário que já foi agendado por um cliente")

        cls.__horarios = [h for h in cls.__horarios if h.get_id() != id_horario]