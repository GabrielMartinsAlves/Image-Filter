# Editor de Imagens com Tkinter e Pillow

Este projeto implementa um editor de imagens simples utilizando a biblioteca `tkinter` para a interface gráfica e a biblioteca `Pillow` (PIL) para manipulação de imagens. Toda a lógica está encapsulada dentro da classe `EditorImagem`, organizada com orientação a objetos.

## Funcionalidades

- **Carregamento de Imagens**: permite ao usuário selecionar e carregar imagens do sistema local em formatos como PNG, JPEG, BMP e GIF.
- **Visualização**: exibe a imagem original e a imagem transformada lado a lado em dois painéis distintos.
- **Filtros e Ajustes**:
  - Aplicar escala de cinza
  - Inverter cores
  - Aumentar contraste
  - Aplicar desfoque
  - Aumentar nitidez
- **Transformações**:
  - Rotacionar 90°
  - Aumentar tamanho da imagem
  - Diminuir tamanho da imagem
  - Ajustar automaticamente à janela de exibição
- **Restauração e Salvamento**:
  - Restaurar a imagem original
  - Salvar a imagem transformada em um novo arquivo

## Organização do Código

O código segue o paradigma de orientação a objetos, centralizando toda a funcionalidade na classe `EditorImagem`. A interface é construída em camadas com uso de `Frame`, `LabelFrame`, `Canvas` e `Button` da biblioteca `tkinter`. A separação das funcionalidades em métodos distintos permite uma melhor organização e facilita a leitura, a manutenção e a expansão do código.

### Principais Métodos da Classe

- `criar_interface()`: monta a interface gráfica.
- `criar_botoes()`: organiza os botões de interação em três linhas.
- `abrir_imagem()`: permite a seleção e abertura de imagens.
- `atualizar_paineis()` e `atualizar_resultado()`: atualizam a visualização das imagens nos painéis.
- `aplicar_escala_cinza()`, `inverter_cores()`, `aplicar_desfoque()`, `aplicar_nitidez()`, `aumentar_contraste()`: aplicam diferentes efeitos visuais.
- `rotacionar_imagem()`, `redimensionar_imagem()`, `ajustar_a_janela()`: realizam transformações geométricas.
- `restaurar_original()`: retorna a imagem ao seu estado inicial.
- `salvar_imagem()`: salva a imagem modificada em um arquivo.

## Vantagens da Orientação a Objetos

A adoção da orientação a objetos neste projeto traz benefícios claros:

- **Organização**: o agrupamento de atributos e métodos em uma única classe facilita o controle do estado e da lógica da aplicação.
- **Reutilização**: métodos bem definidos podem ser reaproveitados em outras partes do projeto ou em projetos futuros.
- **Manutenção**: a estrutura modular permite alterações localizadas sem impacto em outras partes do sistema.
- **Expansão**: é fácil adicionar novas funcionalidades como filtros adicionais ou novas opções de exportação sem comprometer o restante da aplicação.

## Considerações

A interface é simples, limpa e responsiva. O projeto é ideal para quem deseja entender como construir uma aplicação de edição de imagens básica com Python, combinando interface gráfica e processamento de imagens.
