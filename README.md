# INE5421 - Linguagens Formais e Compiladores

**Autores:** Otto Menegasso Pires, Thales Alexandre Zirbel Hübner

Interface Gráfica
-----------------
O programa é composto por uma janela principal onde é possível acessar todas as
funções implementadas. Na barra principal existem dois menus, File e Edit.
 - **File**:Acessando o menu File é possível criar um novo Autômato Finito 
   ou Expressão Regular. Existe também a opção de fechar a aplicação

 - **Edit**:Esse Menu contêm todas as operações que se pode aplicar nos
   Autômatos Finitos ou Expressões Regulares.

Os Autômatos são representados em tabelas e divididos em abas. O autômato cuja
aba esteja selecionada será mostrado na janela. As operações entre dois
autômatos sempre receberão de entrada o autômato atualmente selecionado e um
outro autômato escolhido pelo usuário.

Instruções de Uso
-----------------
 - Para iniciar, basta executar gui. Outra opção é realizar via de comando 'python3 gui.py', mas é necessário python3 e pyqt5 instalados.
 - Ao realizar uma operação entre dois autômatos, certifique-se que eles não
   possuem estados com mesmo nome

 - Ao Inserir o alfabeto de um novo autômato digite todas as letras não
   separadas por espaços ou qualquer outro símbolo. Exemplo: Para inserir o
   alfabeto {a, b, c} digite "abc" no campo especificado.

Partes do Codigo
----------------
Os códigos então divididos da seguinte forma:
- gui.py contém toda a interface gráfica e a invocação dos métodos dos outros módulos/classes
- FA_Algorithms.py têm todos os algoritmos relacionados a autômatos finitos
- Finite_Automata.py é a estrutura que representa um autômato finito e tem algumas funções de alteração de seus conteúdos
- RE_Algorithms.py contêm a estrutura da árvore gerada pelo algoritmo de De Simone e outros algoritmos associados.
