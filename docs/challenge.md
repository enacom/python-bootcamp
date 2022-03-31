# Desafio ENACOM Python bootcamp

## O que será avaliado?
- As dúvidas que foram geradas durante o processo
- A investigação e as possíveis soluções para as dúvidas
- Criação do ambiente de desenvolvimento local
- Testes de unidades implementados
- Estrutura para salvar os resultados da otimização
- Requisição de envio de dados para a rota `/solve`
- Requisição de busca do resultado da otimização de código `code` pela rota `/results/{code}`
- Forma de versionar os códigos com Git e qualidade das mensagens

## Para criar o ambiente de desenvolvimento local

### Códigos fonte
- Crie ou acesse sua conta no [GitHub](https://github.com/)
- Acesse o repositório [https://github.com/enacom/python-bootcamp/](https://github.com/enacom/python-bootcamp/)
- Faça o `fork` desse repositório para sua conta
- Faça o `clone` do seu repositório gerado a partir do fork
- Sincronize seu repositório com o repositório que foi feito o fork sempre que necessário
> O GitHub possui uma documentação sobre isso: [Syncing a fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork)

### Execução em ambientes isolados
A execução da API pode ser feita de dois modos, via Docker / Docker compose (preferível) ou em um ambiente virtual do Python.

#### Docker
```sh
docker compose build
docker compose up
```
ou
```sh
docker compose up --build
```

#### Ambiente virtual Python
Para criar e ativar um ambiente virtual consulte a documentação: [Ambientes virtuais e pacotes](https://docs.python.org/3/tutorial/venv.html)

```sh
uvicorn api.main:api --reload --host 0.0.0.0 --port 9000
```
> Para verificar se a API está ativa acesse:
> [http://0.0.0.0:9000/healthcheck](http://0.0.0.0:9000/healthcheck)
> Se a API estiver ativa, a resposta será: `status	"ok"` ou `{"status":"ok"}`


### Documentação da API
Para acessar a documentação do API abra o seguinte endereço em algum navegador:
[http://0.0.0.0:9000/docs](http://0.0.0.0:9000/docs)
