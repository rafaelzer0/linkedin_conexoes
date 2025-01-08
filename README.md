# Automação de Convites no LinkedIn
Este repositório contém um script em Python que utiliza o Selenium para automatizar o envio de convites no LinkedIn para profissionais de uma determinada área, buscando pelo cargo de interesse. O script facilita a interação com a plataforma para aumentar a rede de contatos.

## Funcionalidade
O script realiza as seguintes etapas:

Login Manual: O usuário realiza o login na conta do LinkedIn manualmente. O script espera até que o login seja concluído.
Pesquisa por Cargo: O script pesquisa pelo cargo de interesse informado (ex: "python") na barra de pesquisa.
Filtragem de Resultados: Após a pesquisa, o script filtra os resultados para mostrar apenas Pessoas.
Envio de Convites: O script percorre a lista de resultados e envia convites de conexão para as pessoas encontradas, com um limite máximo de 15 convites por execução (restrição do LinkedIn).
## Como Funciona
Iniciar o Driver: O script usa o Chrome WebDriver com opções de navegação em modo incógnito e em português.
Login Manual: Após abrir o LinkedIn, o usuário precisa se logar manualmente.
Busca e Filtros: Pesquisa pelo cargo desejado (ex: "python") e aplica o filtro "Pessoas".
Envio de Convites: O script envia convites automaticamente para as pessoas que aparecem nos resultados da pesquisa. O número máximo de convites é 15 para evitar bloqueios temporários da conta.
## Pré-requisitos
Python 3.x
Selenium
WebDriver do Chrome

Instale as dependências necessárias:
pip install selenium

Baixe o Chrome WebDriver:
Faça o download do Chrome WebDriver compatível com sua versão do Google Chrome.



