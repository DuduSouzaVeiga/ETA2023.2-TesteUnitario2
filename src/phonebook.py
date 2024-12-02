class Phonebook:

    def __init__(self):
        self.entries = {'POLICIA': '190'}

    def add(self, name, number):
        """

        :param name: name of person in string
        :param number: number of person in string
        :return: 'Nome invalido' or 'Numero invalido' or 'Numero adicionado'
        """
        # BUG CORRIGIDO: Mensagens escritas erradas
        if any(char in name for char in ['#', '@', '!', '%', '$']):
            return 'Nome invalido'

        # BUGS CORRIGIDOS: If não verificava se o numero estava vazio pois considerava numeros menor que 0, mas
        # string vazia tem tamanho 1 e mensagem estava incorreta
        if len(number) < 1:
            return 'Numero invalido'

        if name not in self.entries:
            self.entries[name] = number

        return 'Numero adicionado'

    def lookup(self, name):
        """
        :param name: name of person in string
        :return: return number of person with name
        """
        # BUG CORRIGIDO: Mensagens escritas erradas
        if any(char in name for char in ['#', '@', '!', '%', '$']):
            return 'Nome invalido'

        # BUG CORRIGIDO: Retorna apenas o numero e nao nome+numero
        return name, self.entries[name]

    def get_names(self):
        """

        :return: return all names in phonebook
        """
        # BUG CORRIGIDO: Retorno deveria ser uma lista, mas retorna dicionario
        return list(self.entries.keys())

    def get_numbers(self):
        """

        :return: return all numbers in phonebook
        """
        # BUG CORRIGIDO: Retorno deveria ser uma lista, mas retorna dicionario
        return list(self.entries.values())

    def clear(self):
        """
        Clear all phonebook
        :return: return 'phonebook limpado'
        """
        self.entries = {}
        return 'phonebook limpado'

    def search(self, search_name):
        """
        Search all substring with search_name
        :param search_name: string with name for search
        :return: return list with results of search
        """
        # BUG CORRIGIDO: If fazia o metodo retornar lista contendo todos os numeros EXCETO o que esta sendo procurado
        result = []
        for name, number in self.entries.items():
            if search_name in name:
                result.append({name, number})
        return result

    def get_phonebook_sorted(self):
        """

        :return: return phonebook in sorted order
        """
        # BUG CORRIGIDO: Retornava dicionario inteiro, deveria retornar todos os nomes em ordem corrigida
        return sorted(self.entries)

    def get_phonebook_reverse(self):
        """

        :return: return phonebook in reverse sorted order
        """
        # BUG CORRIGIDO: Retornava dicionario inteiro, deveria retornar todos os nomes em ordem invertida
        result = sorted(self.entries)
        result.reverse()
        return result

    def delete(self, name):
        """
        Delete person with name
        :param name: String with name
        :return: return 'Numero deletado'
        """
        self.entries.pop(name)
        return 'Numero deletado'

    def change_number(self, name, number):
        if name in self.entries:
            self.entries[name] = number
            return 'Numero alterado com sucesso'
        return 'Contato não encontrado'

    def get_name_by_number(self, number):
        for dic_name, dic_number in self.entries.items():
            if dic_number == number:
                return dic_name
        return 'Numero não encontrado'
