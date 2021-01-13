from django.db import models


class Instituicao(models.Model):
    nome = models.CharField('Nome da Instituição', max_length=50)
    atoDeInscricao = models.CharField('Ato de Inscrição', max_length=100)
    codigoINEP = models.CharField('Código INEP', max_length=10)
    endereco = models.CharField('Endereço', max_length=100)
    bairro = models.CharField('Bairro', max_length=50)
    municipio = models.CharField('Municipio', max_length=20)
    cep = models.CharField('CEP', max_length=10)
    modalidades = models.CharField('Modalidades', max_length=20)

    def __str__(self):
        return self.nome


class Aluno(models.Model):
    username = models.CharField('Nome de Usuario', max_length=50)
    nome = models.CharField('Nome do Aluno', max_length=50)
    dtNascimento = models.DateField('Data de Nascimento')
    rg = models.CharField('RG/RNE/RA', max_length=10)
    nomeMae = models.CharField('Nome da Mãe', max_length=50)
    nomePai = models.CharField('Nome do Pai', max_length=50)
    nivelEnsino = models.CharField('Nível de Ensino', max_length=50)
    anoConclusao = models.DateField('Ano de Conclusão')
    observacoes = models.TextField('Observações')
    instituicao = models.ForeignKey(Instituicao,on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
