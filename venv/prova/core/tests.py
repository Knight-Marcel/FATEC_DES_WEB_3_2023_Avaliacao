from django.test import TestCase
class Presenca(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')
    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)
    def test_texto(self):
        self.assertContains(self.resp, 'index')
    def test_template_natal(self):
        self.assertTemplateUsed(self.resp, 'cadastro.html')    
    def test_cadastro_sucesso(self):
        # Preparação dos dados de teste
        data = {
            'nomealuno': 'João',
            'nomeprofessor': 'Maria',
        }
        
        # Simulando uma requisição POST para a URL de cadastro
        response = self.client.post('/cadastro/', data)
        
        # Verificação do resultado esperado
        self.assertEqual(response.status_code, 200)
        
        # Verificação de que o objeto foi salvo no banco de dados
        self.assertEqual(Presenca.objects.count(), 1)
        presenca = Presenca.objects.first()
        self.assertEqual(presenca.nomealuno, 'João')
        self.assertEqual(presenca.nomeprofessor, 'Maria')
        