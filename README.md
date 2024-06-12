# Atividade de Versionamento
#### Semana 13: Implantação contínua e entrega contínua

## Descrição
Nesta atividade, você praticará seus conhecimentos sobre testes e GitHub Actions. Os passos incluem fazer o fork de um repositório, executar e verificar se os testes estão funcionando corretamente, realizar correções, se necessário, configurar o repositório para executar o GitHub Actions em cada push e enviar o link do GitHub da sua atividade na plataforma AVA.

## Requisitos
* Conta no GitHub
* Conhecimento básico de Python
* Familiaridade com testes unitários

## Passo a Passo
1. Faça um fork do repositório

    Faça o fork do repositório para sua conta no GitHub.

2. Execute os testes:

    Clone o repositório para o seu computador e execute os testes unitários usando o comando:

    ```python -m unittest .\test_pessoa.py```

    Verifique se os testes estão passando com sucesso. Se necessário, faça correções no código pessoa.py.

3. Configure o GitHub Actions:

    O arquivo python.yaml dentro do diretório .github/workflows contém a configuração do GitHub Actions para executar os testes automaticamente em cada push. No entanto, o arquivo ainda não está totalmente implementado, falta os valores de cada chave.

    ### Descrição das chaves
    ```name:``` Nome do workflow, etapa ou passo a passo.

    ```on:``` Define quando o workflow será executado. Neste caso, o workflow será executado em cada push.

    ```jobs:``` Define os jobs que serão executados no workflow.

    ```build:``` Nome do job.

    ```runs-on:``` Define o ambiente de execução do job. Neste caso, o job será executado em um runner do Ubuntu.

    ```steps:``` Define os passos que serão executados no job.

    ```uses:``` Define qual biblioteca do GitHub Actions usar

    ```with:``` Define parametros adicionais para a chave ```uses```

    ```run:``` Executa um comando de terminal

4. Envie o link do GitHub:

    Após completar as etapas anteriores, envie o link do seu repositório GitHub na plataforma AVA.
    
    Semana 13 - Registros 1, 2 e 3

## Referência
* https://github.com/nicolelucena0/Versionamento_S13-main.git
* 
