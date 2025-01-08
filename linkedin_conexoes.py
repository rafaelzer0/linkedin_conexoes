from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as condicao_esperada
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint

# Função para iniciar o driver do Chrome
def iniciar_driver():
    print("Iniciando o driver do Chrome...")  # Log para verificar que a função está sendo chamada
    chrome_options = Options()

    arguments = ['--lang=pt-BR', '--window-size=1100,800', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,
    })

    try:
        # Iniciando o WebDriver
        print("Tentando iniciar o Chrome...")
        driver = webdriver.Chrome(options=chrome_options)
        print("Driver do Chrome iniciado com sucesso!")  # Se chegou até aqui, o driver foi iniciado
    except Exception as e:
        print(f"Erro ao iniciar o driver: {e}")
        return None, None
    wait = WebDriverWait(
        driver,
        10,
        poll_frequency=1,
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException,
        ]
    )
    return driver, wait

# Função principal para automação dos convites no LinkedIn
def automatizar_convites_linkedin(cargo):
    print("Iniciando a automação do LinkedIn...")  # Confirmação de início
    try:
        driver, wait = iniciar_driver()
        if not driver:  # Se o driver não foi iniciado, sai da função
            print("Erro ao iniciar o navegador. Verifique a configuração.")
            return

        # Passo 1: Login no LinkedIn - o usuário fará manualmente
        print("Faça o login no LinkedIn. A automação começará em instantes.")
        driver.get('https://www.linkedin.com/login/pt?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
        sleep(40)  # Tempo para o usuário fazer login manualmente

        # Passo 2: Pesquisa pela profissão (cargo)
        campo_pesquisar = wait.until(condicao_esperada.visibility_of_element_located((By.XPATH, "//input[@placeholder='Pesquisar']")))
        campo_pesquisar.click()
        sleep(randint(1, 4))

        campo_pesquisar.send_keys(cargo)
        sleep(randint(1, 3))
        campo_pesquisar.send_keys(Keys.ENTER)
        sleep(randint(10, 15))

        # Passo 3: Filtrar por "Pessoas"
        campo_pessoas = wait.until(condicao_esperada.visibility_of_all_elements_located((By.XPATH, "//button[text()='Pessoas']")))
        campo_pessoas[0].click()
        sleep(randint(4, 8))

    except Exception as e:
        print(f"Erro durante a automação: {e}")
        return

    qtd_convites = 0  # Contador de convites enviados
    while True:
        # Passo 4: Rolando a página para enviar convites
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(4)
        driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
        sleep(4)

        if qtd_convites < 15:
            try:
                # Verificar se há botões "Conectar"
                botoes_conectar = wait.until(condicao_esperada.presence_of_all_elements_located((By.XPATH, "//button//span[text()='Conectar']")))
                for botao in botoes_conectar:
                    if qtd_convites < 15:
                        # Clicar no primeiro botão "Conectar"
                        botao.click()
                        sleep(randint(5, 10))

                        # Espera explicita para o botão de enviar o convite
                        botao_enviar_sem_nota = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//button[@aria-label="Enviar sem nota"]')))
                        botao_enviar_sem_nota.click()
                        print(f'Convite enviado.')
                        sleep(randint(2, 7))
                        qtd_convites += 1
                    else:
                        print("Limite de convites diário atingido.")
                        driver.quit()
                        return

            except Exception as e:
                print(f"Erro ao tentar enviar convite: {e}")
                driver.quit()  # Fecha o navegador se um erro ocorrer
                break

        else:
            print(f"Limite de convites diário atingido ({qtd_convites} convites enviados).")
            driver.quit()  # Fecha o navegador quando o limite de convites for alcançado
            break

# Exemplo de uso:
cargo = 'python'  # Cargo para buscar
automatizar_convites_linkedin(cargo)
