# FinDataViz: Dashboard de Análise de Dados Financeiros

## Visão Geral
FinDataViz é um dashboard interativo construído usando Django, projetado para fornecer análises visuais de dados financeiros. Ele integra dados em tempo real através da API Alpha Vantage, permitindo aos usuários visualizar e analisar as tendências do mercado de ações com uma variedade de gráficos dinâmicos.

## Funcionalidades

- **Visualização em Tempo Real**: Gráficos atualizados continuamente com dados mais recentes do mercado.
- **Tipos de Gráficos**: Inclui gráficos de linhas, barras e rosca para diferentes perspectivas de análise.
- **Responsividade**: Interface limpa e responsiva, adequada para todos os dispositivos.
- **Customização**: Opções para personalizar os gráficos de acordo com as preferências do usuário.

## Tecnologias Utilizadas

- **Frontend**: HTML, CSS para estilização e JavaScript para funcionalidades interativas.
- **Gráficos**: Utiliza Chart.js para a renderização de gráficos.
- **Backend**: Desenvolvido com Django, Python.
- **APIs**: Dados obtidos via Alpha Vantage.

## Instalação

Para configurar e executar o projeto localmente, siga os passos abaixo:

# Clone o repositório
git clone https://github.com/seu_usuario/FinDataViz.git
cd FinDataViz

# Instale as dependências
pip install -r requirements.txt

# Execute as migrações
python manage.py migrate

# Inicie o servidor
python manage.py runserver

Acesse http://127.0.0.1:8000/ para ver o aplicativo em ação.

# Contribuindo

Contribuições são o que fazem a comunidade open source um lugar incrível para aprender, inspirar e criar. Todas as contribuições que você fizer são muito apreciadas.

1. Faça um Fork do projeto
2. Crie sua Feature Branch (git checkout -b feature/AmazingFeature)
3. Faça commit das suas mudanças (git commit -m 'Add some AmazingFeature')
4. Faça Push para a Branch (git push origin feature/AmazingFeature)
5. Abra um Pull Request
