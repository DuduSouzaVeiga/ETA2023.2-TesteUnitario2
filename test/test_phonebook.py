from src.phonebook import Phonebook


class TestPhonebook:

    def test_add_success(self):
        expected_result = 'Numero adicionado'
        phonebook = Phonebook()
        result = phonebook.add('SAMU', '192')
        assert result == expected_result

    def test_add_invalid_name_sharp(self):
        expected_result = 'Nome invalido'
        phonebook = Phonebook()
        result = phonebook.add('S#MU', '192')
        assert result == expected_result

    def test_add_invalid_name_at(self):
        expected_result = 'Nome invalido'
        phonebook = Phonebook()
        result = phonebook.add('S@MU', '192')
        assert result == expected_result

    def test_add_invalid_name_dollar(self):
        expected_result = 'Nome invalido'
        phonebook = Phonebook()
        result = phonebook.add('$AMU', '192')
        assert result == expected_result

    def test_add_invalid_name_exclamation(self):
        expected_result = 'Nome invalido'
        phonebook = Phonebook()
        result = phonebook.add('SAMU!', '192')
        assert result == expected_result

    def test_add_invalid_name_percentage(self):
        expected_result = 'Nome invalido'
        phonebook = Phonebook()
        result = phonebook.add('SAMU%', '192')
        assert result == expected_result

    def test_lookup_invalid_name_sharp(self):
        expected_result = 'Nome invalido'
        phonebook = Phonebook()
        result = phonebook.lookup('S#MU')
        assert result == expected_result

    def test_lookup_invalid_name_at(self):
        expected_result = 'Nome invalido'
        phonebook = Phonebook()
        result = phonebook.lookup('S@MU')
        assert result == expected_result

    def test_lookup_invalid_name_dollar(self):
        expected_result = 'Nome invalido'
        phonebook = Phonebook()
        result = phonebook.lookup('$AMU')
        assert result == expected_result

    def test_lookup_invalid_name_exclamation(self):
        expected_result = 'Nome invalido'
        phonebook = Phonebook()
        result = phonebook.lookup('SAMU!')
        assert result == expected_result

    def test_lookup_invalid_name_percentage(self):
        expected_result = 'Nome invalido'
        phonebook = Phonebook()
        result = phonebook.lookup('SAMU%')
        assert result == expected_result

    def test_add_empty_number(self):
        expected_result = 'Numero invalido'
        phonebook = Phonebook()
        result = phonebook.add('SAMU', '')
        assert result == expected_result

    def test_delete_from_phonebook(self):
        expected_result = 'Numero deletado'
        phonebook = Phonebook()
        phonebook.add('CTTU', '123')
        result = phonebook.delete('CTTU')
        assert result == expected_result

    def test_clear_phonebook(self):
        expected_result = 'phonebook limpado'
        phonebook = Phonebook()
        result = phonebook.clear()
        assert result == expected_result

    def test_search_phonebook(self):
        expected_result = [{'Andre', '192'}, {'Andrea', '123'}, {'Andreia', '1233'}]
        phonebook = Phonebook()
        phonebook.add('Andre', '192')
        phonebook.add('Andrea', '123')
        phonebook.add('Andreia', '1233')
        result = phonebook.search('Andre')
        assert result == expected_result

    def test_lookup_phonebook(self):
        expected_result = ('SAMU', '192')
        phonebook = Phonebook()
        phonebook.add('SAMU', '192')
        phonebook.add('CTTU', '123')
        result = phonebook.lookup('SAMU')
        assert result == expected_result

    def test_get_names(self):
        expected_result = ['POLICIA', 'SAMU', 'CTTU']
        phonebook = Phonebook()
        phonebook.add('SAMU', '192')
        phonebook.add('CTTU', '123')
        result = phonebook.get_names()
        assert result == expected_result

    def test_get_numbers(self):
        expected_result = ['190', '192', '123']
        phonebook = Phonebook()
        phonebook.add('SAMU', '192')
        phonebook.add('CTTU', '123')
        result = phonebook.get_numbers()
        assert result == expected_result

    def test_get_phonebook_sorted(self):
        expected_result = ['CTTU', 'POLICIA', 'SAMU']
        phonebook = Phonebook()
        phonebook.add('SAMU', '192')
        phonebook.add('CTTU', '123')
        result = phonebook.get_phonebook_sorted()
        assert result == expected_result

    def test_get_phonebook_reverse(self):
        expected_result = ['SAMU', 'POLICIA', 'CTTU' ]
        phonebook = Phonebook()
        phonebook.add('SAMU', '192')
        phonebook.add('CTTU', '123')
        result = phonebook.get_phonebook_reverse()
        assert result == expected_result

    def test_get_name_by_number(self):
        expected_result = 'SAMU'
        phonebook = Phonebook()
        phonebook.add('SAMU', '192')
        result = phonebook.get_name_by_number('192')
        assert result == expected_result

    def test_get_name_by_nonexistent_number(self):
        expected_result = 'Numero não encontrado'
        phonebook = Phonebook()
        result = phonebook.get_name_by_number('192')
        assert result == expected_result

    def test_change_number(self):
        expected_result = "Numero alterado com sucesso"
        phonebook = Phonebook()
        phonebook.add('SAMU', '123')
        result = phonebook.change_number('SAMU', '192')
        assert result == expected_result

    def test_change_nonexistent_number(self):
        expected_result = 'Contato não encontrado'
        phonebook = Phonebook()
        result = phonebook.change_number('SAMU', '192')
        assert result == expected_result
