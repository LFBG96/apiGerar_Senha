# apiGerar_Senha
<p>Essa api possui apenas 1 endpoint que é "/senha/"</p>
<p>Para aumentar a quantidade de caracteres gerados precisa adicionar um int depois da "/"</p>
<p>Nesse projeto utilizei 4 bibliotecas sendo 2 do proprio python e 2 externas sendo elas</p>
<h3>Bibliotecas python</h3>
<ul>
  <li>secrets</li>
  <li>random</li>
</ul>
<h3>Bibliotecas externas</h3>
<ul>
  <li>flask</li>
  <li>flask_cors</li>
</ul>
<p>A biblioteca secrets utilizei para gerar um token utlizados em html pois ele cria ja com letras minusculas, maiusculas e alguns caracteres especiais</p>
<p>A random foi utilizada para inserir novos caracteres em posições aleatorios dentro do token gerado pelo secrets</p>
<p>flask foi utilizado para fazer a api funcionar</p>
<p>flask_cors foi utilizada para mostrar os dados no browser </p>
