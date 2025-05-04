from nao_trivial_automator import NonTrivialAutomator
from utils.opcoes import MenuDeOpcoes
import pyautogui as pg
import time

class NonTrivialSystem:
    def __init__(self):
        self.automator = NonTrivialAutomator()
        self.menus = MenuDeOpcoes()
        self.delay = 1  # Delay padrão entre ações

    def solicitar_entrada(self, prompt, opcoes_validas):
        while True:
            entrada = input(prompt).strip()
            if entrada in opcoes_validas:
                return entrada
            print("\033[31mOpção inválida. Tente novamente.\033[0m")

    def executar_com_seguranca(self, funcao, *args):
        try:
            funcao(*args)
        except Exception as e:
            print(f"\033[31mErro na execução: {str(e)}\033[0m")
            pg.alert(f"Erro na automação: {str(e)}")

    # Métodos principais de automação
    def iniciar_ambiente_trabalho(self):
        print("Iniciando ambiente de trabalho...")
        self.executar_com_seguranca(self.automator.abrir_navegador, "https://www.canva.com/")
        time.sleep(self.delay)
        self.executar_com_seguranca(self.automator.fazer_login_canva)

    def gerenciar_projetos_canva(self):
        opcoes = {
            '1': ("Procurar projeto", self.automator.procurar_projeto),
            '2': ("Excluir projeto", self.automator.excluir_projeto),
            '3': ("Duplicar projeto", self.automator.duplicar_projeto)
        }
        # Lógica para submenu

    def menu_downloads(self):
        print("Opções de download:")
        self.executar_com_seguranca(self.automator.baixar_projeto, "ultima_versao")

def main():
    sistema = NonTrivialSystem()
    
    while True:
        print("\n=== Menu Principal Não Trivial ===")
        sistema.menus.exibir_menu_principal()
        opcao = sistema.solicitar_entrada("Escolha uma opção (1-6): ", [str(i) for i in range(1, 7)])

        opcoes = {
            '1': ("🚀 Iniciar Ambiente de Trabalho", sistema.iniciar_ambiente_trabalho),
            '2': ("🎨 Gerenciar Projetos Canva", sistema.gerenciar_projetos_canva),
            '3': ("📥 Downloads Automáticos", sistema.menu_downloads),
            '4': ("📆 Agendar Publicações", sistema.automator.agendar_publicacoes),
            '5': ("📊 Analisar Métricas", sistema.automator.analisar_metricas),
            '6': ("❌ Sair do Sistema", exit)
        }

        print(f"\nExecutando: {opcoes[opcao][0]}...")
        opcoes[opcao][1]()

if __name__ == "__main__":
    main()