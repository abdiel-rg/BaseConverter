<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>README</title>
  <link rel="stylesheet" href="https://stackedit.io/style.css" />
</head>

<body class="stackedit">
  <div class="stackedit__html"><h1 id="conversor-de-sistemas-numéricos-en-python-snake">Conversor de Sistemas Numéricos en Python 🐍</h1>
<p>Primero, importamos los módulos necesarios para el funcionamiento del programa.</p>
<pre class=" language-python"><code class="prism  language-python"><span class="token keyword">from</span> functools <span class="token keyword">import</span> <span class="token builtin">reduce</span>
<span class="token keyword">from</span> multipledispatch <span class="token keyword">import</span> dispatch
</code></pre>
<p>Cabe destacar que no usaremos estos módulos para hacer la conversión en sí sino, mas bien, para agregar funcionalidades útiles tales como <code>reduce</code> y sobrecarga de métodos.</p>
<p>Declaramos una variable de tipo <code>string</code> que almacenará los valores equivalentes de cada carácter.</p>
<pre class=" language-python"><code class="prism  language-python">equivalences <span class="token operator">=</span> <span class="token string">"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"</span>
</code></pre>
<p>La <em>base mínima</em> que podemos convertir es <strong>2</strong>.<br>
La <em>base máxima</em> sería la longitud de la variable <code>equivalences</code> que, en este caso, es <strong>36</strong>.</p>
<pre class=" language-python"><code class="prism  language-python"><span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> <span class="token builtin">len</span><span class="token punctuation">(</span>equivalences<span class="token punctuation">)</span>
<span class="token number">36</span>
</code></pre>
<br>
<h2 id="convirtiendo-de-decimal-a-cualquier-base">Convirtiendo de Decimal a cualquier Base</h2>
<pre class=" language-python"><code class="prism  language-python"><span class="token keyword">def</span>  <span class="token function">dec_to_base</span><span class="token punctuation">(</span>num<span class="token punctuation">:</span> <span class="token builtin">int</span><span class="token punctuation">,</span> to_base<span class="token punctuation">:</span> <span class="token builtin">int</span><span class="token punctuation">)</span> <span class="token operator">-</span><span class="token operator">&gt;</span> <span class="token builtin">str</span><span class="token punctuation">:</span>
</code></pre>
<p>Definimos la función <code>dec_to_base</code> que toma como parámetros, ambos de tipo entero:</p>
<ul>
<li><code>num</code>, el número que queremos convertir</li>
<li><code>to_base</code>, la base a la que queremos convertir</li>
</ul>
<p>Esta función retorna una representación textual del número en la base especificada .</p>
<p>Llamamos a la función <code>valid_base</code> (el cual definiremos más adelante) para validar si la base cumple con los parámetros.</p>
<pre class=" language-python"><code class="prism  language-python">valid_base<span class="token punctuation">(</span>to_base<span class="token punctuation">)</span>
</code></pre>
<p>A continuación, definimos una variable <code>result</code> de tipo <code>list</code> que almacenara el resultado de la conversión.</p>
<pre class=" language-python"><code class="prism  language-python">result <span class="token operator">=</span> <span class="token punctuation">[</span><span class="token punctuation">]</span>
</code></pre>
<p>Haremos uso de un ciclo <code>while</code> para obtener cada uno de los elementos de nuestro resultado.</p>
<pre class=" language-python"><code class="prism  language-python"><span class="token keyword">while</span> num <span class="token operator">&gt;</span> <span class="token number">0</span><span class="token punctuation">:</span>
	calc <span class="token operator">=</span> num <span class="token operator">%</span> to_base
	result<span class="token punctuation">.</span>append<span class="token punctuation">(</span>equivalences<span class="token punctuation">[</span>calc<span class="token punctuation">]</span> <span class="token operator">or</span> calc<span class="token punctuation">)</span>
	num <span class="token operator">=</span> <span class="token builtin">int</span><span class="token punctuation">(</span>num <span class="token operator">/</span> to_base<span class="token punctuation">)</span>
</code></pre>
<p>Dentro del ciclo <code>while</code>:</p>
<ol>
<li>
<p>La variable <code>calc</code> almacena el resultado de la operación módulo, la cuál  retorna el residuo de la división de <code>num</code> y <code>to_base</code>.</p>
<pre class=" language-python"><code class="prism  language-python">calc <span class="token operator">=</span> num <span class="token operator">%</span> to_base
</code></pre>
<p>Suponiendo que <code>num</code> sea igual a <strong>25</strong> y <code>to_base</code> sea igual a <strong>4</strong>:</p>
<pre class=" language-python"><code class="prism  language-python"><span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> num <span class="token operator">%</span> to_base
<span class="token number">1</span>
</code></pre>
</li>
<li>
<p>Agregamos el resultado de la siguiente operación al final de la lista <code>result</code>:</p>
<pre class=" language-python"><code class="prism  language-python">result<span class="token punctuation">.</span>append<span class="token punctuation">(</span>equivalences<span class="token punctuation">[</span>calc<span class="token punctuation">]</span> <span class="token operator">or</span> calc<span class="token punctuation">)</span>
</code></pre>
<ul>
<li>
<p>Si la lista <code>equivalences</code> contiene un elemento cuyo índice es el valor de <code>calc</code>, se devuelve dicho elemento, por ejemplo:</p>
<pre class=" language-python"><code class="prism  language-python"><span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> equivalences<span class="token punctuation">[</span><span class="token number">0</span><span class="token punctuation">]</span>
<span class="token number">0</span>
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> equivalences<span class="token punctuation">[</span><span class="token number">11</span><span class="token punctuation">]</span>
<span class="token string">"A"</span>
</code></pre>
</li>
<li>
<p>Si no, se devuelve el valor de <code>calc</code>.</p>
</li>
</ul>
</li>
<li>
<p>Asignamos a <code>num</code> el valor de la división de <code>num</code> entre <code>to_base</code>, sin la parte decimal.</p>
<pre class=" language-python"><code class="prism  language-python">num <span class="token operator">=</span> <span class="token builtin">int</span><span class="token punctuation">(</span>num <span class="token operator">/</span> to_base<span class="token punctuation">)</span>
</code></pre>
<p>Suponiendo que <code>num</code> sea igual a <strong>26</strong> y <code>to_base</code> sea igual a <strong>4</strong>:</p>
<pre class=" language-python"><code class="prism  language-python"><span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> num <span class="token operator">/</span> to_base
<span class="token number">6.5</span>

<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> <span class="token builtin">int</span><span class="token punctuation">(</span>num <span class="token operator">/</span> to_base<span class="token punctuation">)</span>
<span class="token number">6</span> 
</code></pre>
</li>
</ol>
<p>Finalmente, retornamos la lista en orden inverso y convertida a tipo <code>str</code>.</p>
<pre class=" language-python"><code class="prism  language-python"><span class="token keyword">return</span>  <span class="token string">""</span><span class="token punctuation">.</span>join<span class="token punctuation">(</span>result<span class="token punctuation">.</span>__reversed__<span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">)</span>
</code></pre>
<br>
<h3 id="función-dec_to_base-completa">Función <code>dec_to_base</code> completa</h3>
<pre class=" language-python"><code class="prism  language-python"><span class="token keyword">def</span>  <span class="token function">dec_to_base</span><span class="token punctuation">(</span>num<span class="token punctuation">:</span> <span class="token builtin">int</span><span class="token punctuation">,</span> to_base<span class="token punctuation">:</span> <span class="token builtin">int</span><span class="token punctuation">)</span> <span class="token operator">-</span><span class="token operator">&gt;</span> <span class="token builtin">str</span><span class="token punctuation">:</span>
	valid_base<span class="token punctuation">(</span>to_base<span class="token punctuation">)</span>
	result <span class="token operator">=</span> <span class="token punctuation">[</span><span class="token punctuation">]</span>
	<span class="token keyword">while</span> num <span class="token operator">&gt;</span> <span class="token number">0</span><span class="token punctuation">:</span>
		calc <span class="token operator">=</span> num <span class="token operator">%</span> to_base
		result<span class="token punctuation">.</span>append<span class="token punctuation">(</span>equivalences<span class="token punctuation">[</span>calc<span class="token punctuation">]</span> <span class="token operator">or</span> calc<span class="token punctuation">)</span>
		num <span class="token operator">=</span> <span class="token builtin">int</span><span class="token punctuation">(</span>num <span class="token operator">/</span> to_base<span class="token punctuation">)</span>
	<span class="token keyword">return</span>  <span class="token string">""</span><span class="token punctuation">.</span>join<span class="token punctuation">(</span>result<span class="token punctuation">.</span>__reversed__<span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">)</span>
</code></pre>
<br>
<h2 id="convirtiendo-de-cualquier-base-a-decimal">Convirtiendo de cualquier Base a Decimal</h2>
<p>Definimos la función <code>base_to_dec</code> que toma como parámetros:</p>
<ul>
<li><code>num</code>, la representación textual del número que queremos convertir</li>
<li><code>to_base</code>, la base del numero guardado en <code>num</code></li>
</ul>
<p>Esta función retorna el numero convertido a base 10.</p>
<pre class=" language-python"><code class="prism  language-python"><span class="token keyword">def</span> <span class="token function">base_to_dec</span><span class="token punctuation">(</span>num<span class="token punctuation">:</span> <span class="token builtin">str</span><span class="token punctuation">,</span> from_base<span class="token punctuation">:</span> <span class="token builtin">int</span><span class="token punctuation">)</span> <span class="token operator">-</span><span class="token operator">&gt;</span> <span class="token builtin">int</span><span class="token punctuation">:</span>
</code></pre>
<p>Llamamos a la función <code>valid_base</code> (el cual definiremos más adelante) para validar si la base cumple con los parámetros.</p>
<pre class=" language-python"><code class="prism  language-python">valid_base<span class="token punctuation">(</span>from_base<span class="token punctuation">)</span>
</code></pre>
<p>Declaramos la variable <code>string_list</code> de tipo <code>map</code> que recorre <code>num</code> y, por medio de una función<sup class="footnote-ref"><a href="#fn1" id="fnref1">1</a></sup>, crea una nueva lista cuyos valores son los índices de cada elemento en <code>equivalences</code>.</p>
<pre class=" language-python"><code class="prism  language-python">string_list <span class="token operator">=</span> <span class="token builtin">map</span><span class="token punctuation">(</span><span class="token keyword">lambda</span>  x<span class="token punctuation">:</span> equivalences<span class="token punctuation">.</span>find<span class="token punctuation">(</span>x<span class="token punctuation">)</span><span class="token punctuation">,</span> num<span class="token punctuation">)</span>
</code></pre>
<p>Esto tiene el efecto de <em>“traducir”</em> el carácter a su número correspondiente:</p>
<pre class=" language-python"><code class="prism  language-python">num <span class="token operator">=</span> <span class="token string">"9C4"</span>
string_list <span class="token operator">=</span> <span class="token punctuation">[</span> <span class="token number">9</span><span class="token punctuation">,</span> <span class="token number">12</span><span class="token punctuation">,</span> <span class="token number">4</span> <span class="token punctuation">]</span>
</code></pre>
<p>Retornamos el resultado de un método<sup class="footnote-ref"><a href="#fn2" id="fnref2">2</a></sup> <code>reduce</code> con los siguientes parámetros:</p>
<pre class=" language-python"><code class="prism  language-python"><span class="token keyword">return</span> <span class="token builtin">reduce</span><span class="token punctuation">(</span>
<span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">.</span>
<span class="token punctuation">)</span>
</code></pre>
<ul>
<li>
<p>Una función<sup class="footnote-ref"><a href="#fn1" id="fnref1:1">1</a></sup>, repetida por cada elemento de <code>string_list</code>, que recibe dos parámetros:</p>
<ul>
<li><code>acc</code>: variable acumulativa</li>
<li><code>curr</code>: elemento actual</li>
</ul>
<pre class=" language-python"><code class="prism  language-python"><span class="token keyword">lambda</span>  acc<span class="token punctuation">,</span> curr<span class="token punctuation">:</span> acc <span class="token operator">+</span> curr<span class="token punctuation">[</span><span class="token number">1</span><span class="token punctuation">]</span> <span class="token operator">*</span> from_base <span class="token operator">**</span> <span class="token punctuation">(</span><span class="token builtin">len</span><span class="token punctuation">(</span>num<span class="token punctuation">)</span> <span class="token operator">-</span> curr<span class="token punctuation">[</span><span class="token number">0</span><span class="token punctuation">]</span> <span class="token operator">-</span> <span class="token number">1</span><span class="token punctuation">)</span><span class="token punctuation">,</span>
</code></pre>
<p>Y ejecuta la siguiente operación</p>
<blockquote>
<p><span class="katex--inline"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mi mathvariant="bold-italic">a</mi><mo mathvariant="bold-italic">+</mo><msub><mi mathvariant="bold-italic">c</mi><mn mathvariant="bold-italic">1</mn></msub><mo mathvariant="bold-italic">⋅</mo><msup><mi mathvariant="bold-italic">b</mi><mrow><mo stretchy="false">(</mo><mi mathvariant="bold-italic">l</mi><mo mathvariant="bold-italic">−</mo><msub><mi mathvariant="bold-italic">c</mi><mn mathvariant="bold-italic">0</mn></msub><mo mathvariant="bold-italic">−</mo><mn mathvariant="bold-italic">1</mn><mo stretchy="false">)</mo></mrow></msup></mrow></mrow><annotation encoding="application/x-tex">\boldsymbol{a+c_{1} \cdot b^{(l-c_{0}-1)}}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 1.038em; vertical-align: -0.15em;"></span><span class="mord"><span class="mord"><span class="mord boldsymbol">a</span><span class="mspace" style="margin-right: 0.222222em;"></span><span class="mbin mathbf">+</span><span class="mspace" style="margin-right: 0.222222em;"></span><span class="mord"><span class="mord boldsymbol">c</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.301108em;"><span class="" style="top: -2.55em; margin-left: 0em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathbf mtight">1</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.15em;"><span class=""></span></span></span></span></span></span><span class="mspace" style="margin-right: 0.222222em;"></span><span class="mbin mathbf">⋅</span><span class="mspace" style="margin-right: 0.222222em;"></span><span class="mord"><span class="mord boldsymbol">b</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height: 0.888em;"><span class="" style="top: -3.063em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mopen mathbf mtight">(</span><span class="mord boldsymbol mtight" style="margin-right: 0.0088em;">l</span><span class="mbin mathbf mtight">−</span><span class="mord mtight"><span class="mord boldsymbol mtight">c</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.317314em;"><span class="" style="top: -2.357em; margin-left: 0em; margin-right: 0.0714286em;"><span class="pstrut" style="height: 2.5em;"></span><span class="sizing reset-size3 size1 mtight"><span class="mord mtight"><span class="mord mathbf mtight">0</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.143em;"><span class=""></span></span></span></span></span></span><span class="mbin mathbf mtight">−</span><span class="mord mathbf mtight">1</span><span class="mclose mathbf mtight">)</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><br>
<strong>Dónde</strong>:<br>
a = acc<br>
c<sub>0</sub> = curr[0]  = índice del elemento actual<br>
c<sub>1</sub>= curr[1] = valor del elemento actual<br>
b = valor de <code>from_base</code><br>
l = len(num) = longitud de la variable <code>num</code></p>
</blockquote>
<p>…sumando todos los elementos.</p>
<p>Por ejemplo:</p>
<pre class=" language-python"><code class="prism  language-python"><span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> <span class="token builtin">reduce</span><span class="token punctuation">(</span><span class="token keyword">lambda</span> a<span class="token punctuation">,</span>b<span class="token punctuation">:</span> a<span class="token operator">+</span>b<span class="token punctuation">,</span><span class="token punctuation">[</span><span class="token number">1</span><span class="token punctuation">,</span> <span class="token number">2</span><span class="token punctuation">,</span> <span class="token number">3</span><span class="token punctuation">]</span><span class="token punctuation">,</span> <span class="token number">0</span><span class="token punctuation">)</span>
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> <span class="token number">6</span>
</code></pre>
</li>
<li>
<p>Un método<sup class="footnote-ref"><a href="#fn3" id="fnref3">3</a></sup> que, para cada elemento, devuelve un objeto que contiene el índice, en el posición 0; el valor, en la posición 1; entre otras cosas.</p>
<pre class=" language-python"><code class="prism  language-python"><span class="token builtin">enumerate</span><span class="token punctuation">(</span>string_list<span class="token punctuation">)</span>
</code></pre>
</li>
<li>
<p>El estado inicial de la variable <code>acc</code> que, en este caso, seria <strong>0</strong>.</p>
</li>
</ul>
<br>
<h3 id="funciónbase_to_dec-completa">Función<code>base_to_dec</code> completa</h3>
<pre class=" language-python"><code class="prism  language-python"><span class="token keyword">def</span>  <span class="token function">base_to_dec</span><span class="token punctuation">(</span>num<span class="token punctuation">:</span> <span class="token builtin">str</span><span class="token punctuation">,</span> from_base<span class="token punctuation">:</span> <span class="token builtin">int</span><span class="token punctuation">)</span> <span class="token operator">-</span><span class="token operator">&gt;</span> <span class="token builtin">int</span><span class="token punctuation">:</span>
	string_list <span class="token operator">=</span> <span class="token builtin">map</span><span class="token punctuation">(</span><span class="token keyword">lambda</span>  x<span class="token punctuation">:</span> equivalences<span class="token punctuation">.</span>find<span class="token punctuation">(</span>x<span class="token punctuation">)</span><span class="token punctuation">,</span> num<span class="token punctuation">)</span>
	<span class="token keyword">return</span>  <span class="token builtin">reduce</span><span class="token punctuation">(</span>
					<span class="token keyword">lambda</span>  acc<span class="token punctuation">,</span> curr<span class="token punctuation">:</span> acc <span class="token operator">+</span> curr<span class="token punctuation">[</span><span class="token number">1</span><span class="token punctuation">]</span> <span class="token operator">*</span> from_base <span class="token operator">**</span> <span class="token punctuation">(</span><span class="token builtin">len</span><span class="token punctuation">(</span>num<span class="token punctuation">)</span> <span class="token operator">-</span> curr<span class="token punctuation">[</span><span class="token number">0</span><span class="token punctuation">]</span> <span class="token operator">-</span> <span class="token number">1</span><span class="token punctuation">)</span><span class="token punctuation">,</span>
					<span class="token builtin">enumerate</span><span class="token punctuation">(</span>string_list<span class="token punctuation">)</span><span class="token punctuation">,</span>
					<span class="token number">0</span>
				<span class="token punctuation">)</span>
</code></pre>
<br>
<h2 id="evitando-errores">Evitando errores</h2>
<p>Definiremos una función corta que solo se encargará de confirmar, para cada base que le pasemos como parámetro <code>int</code>, si es <em>mayor o igual que</em> <strong>2</strong> o <em>menor o igual</em> a la longitud de la variable <code>equivalences</code>.</p>
<pre class=" language-python"><code class="prism  language-python"><span class="token keyword">def</span>  <span class="token function">valid_base</span><span class="token punctuation">(</span><span class="token operator">*</span>bases<span class="token punctuation">:</span> <span class="token builtin">int</span><span class="token punctuation">)</span><span class="token punctuation">:</span>	
	<span class="token keyword">for</span> base <span class="token keyword">in</span> bases<span class="token punctuation">:</span>
		<span class="token keyword">if</span> base <span class="token operator">&lt;</span> <span class="token number">2</span>  <span class="token operator">or</span> base <span class="token operator">&gt;</span> <span class="token builtin">len</span><span class="token punctuation">(</span>equivalences<span class="token punctuation">)</span><span class="token punctuation">:</span>
			<span class="token keyword">raise</span>  IndexError<span class="token punctuation">(</span>f<span class="token string">"Base must be higher or equal to 2 and lower or equal to {len(equivalences)}"</span><span class="token punctuation">)</span>
</code></pre>
<br>
<h2 id="combinando-todo">Combinando todo</h2>
<p>Definimos la función  <code>converter</code>, que hará uso de las funciones anteriores para convertir de decimal a cualquier base y, además, sera sobrecargada más adelante para permitir la conversión de cualquier base a cualquier base.</p>
<p>Recibe los parámetros:</p>
<ul>
<li><code>num</code>: numero en base 10, de tipo  <code>int</code>,</li>
<li><code>to_base</code>: la base a la que se quiere convertir</li>
</ul>
<p>Devuelve una representación textual del número convertido a la base especificada.</p>
<pre class=" language-python"><code class="prism  language-python"><span class="token keyword">def</span>  <span class="token function">converter</span><span class="token punctuation">(</span>num<span class="token punctuation">:</span> <span class="token builtin">int</span><span class="token punctuation">,</span> to_base<span class="token punctuation">:</span> <span class="token builtin">int</span><span class="token punctuation">)</span> <span class="token operator">-</span><span class="token operator">&gt;</span> <span class="token builtin">str</span><span class="token punctuation">:</span>
	<span class="token keyword">return</span> dec_to_base<span class="token punctuation">(</span>num<span class="token punctuation">,</span> to_base<span class="token punctuation">)</span>
</code></pre>
<p>Una línea antes de la declaración de la función, agregamos el decorador…</p>
<pre class=" language-python"><code class="prism  language-python">@dispatch<span class="token punctuation">(</span><span class="token builtin">int</span><span class="token punctuation">,</span> <span class="token builtin">int</span><span class="token punctuation">)</span>
</code></pre>
<p>…con sus respectivos parámetros, para que la función correcta sea seleccionada en tiempo de ejecución.</p>
<h3 id="función-converter-completa">Función <code>converter</code> completa</h3>
<pre class=" language-python"><code class="prism  language-python">@dispatch<span class="token punctuation">(</span><span class="token builtin">int</span><span class="token punctuation">,</span> <span class="token builtin">int</span><span class="token punctuation">)</span>
<span class="token keyword">def</span>  <span class="token function">converter</span><span class="token punctuation">(</span>num<span class="token punctuation">:</span> <span class="token builtin">int</span><span class="token punctuation">,</span> to_base<span class="token punctuation">:</span> <span class="token builtin">int</span><span class="token punctuation">)</span> <span class="token operator">-</span><span class="token operator">&gt;</span> <span class="token builtin">str</span><span class="token punctuation">:</span>
	<span class="token keyword">return</span> dec_to_base<span class="token punctuation">(</span>num<span class="token punctuation">,</span> to_base<span class="token punctuation">)</span>
</code></pre>
<br>
<h2 id="sobrecargando-la-función-converter">Sobrecargando la función <code>converter</code></h2>
<p>Finalmente, sobrecargamos la función  <code>converter</code>, para que nos permita convertir de cualquier base a cualquier base.</p>
<p>Recibe los parámetros:</p>
<ul>
<li><code>num</code>:  representación textual del número que queremos convertir,</li>
<li><code>from_base</code>: la base del numero que queremos convertir</li>
<li><code>to_base</code>: la base a la que se quiere convertir</li>
</ul>
<p>Devuelve una representación textual del número convertido a la base especificada.</p>
<pre class=" language-python"><code class="prism  language-python"><span class="token keyword">def</span>  <span class="token function">converter</span><span class="token punctuation">(</span>num<span class="token punctuation">:</span> <span class="token builtin">str</span><span class="token punctuation">,</span> from_base<span class="token punctuation">:</span> <span class="token builtin">int</span><span class="token punctuation">,</span> to_base<span class="token punctuation">:</span> <span class="token builtin">int</span><span class="token punctuation">)</span> <span class="token operator">-</span><span class="token operator">&gt;</span> <span class="token builtin">str</span><span class="token punctuation">:</span>
	<span class="token keyword">return</span> dec_to_base<span class="token punctuation">(</span>base_to_dec<span class="token punctuation">(</span>num<span class="token punctuation">,</span> from_base<span class="token punctuation">)</span><span class="token punctuation">,</span> to_base<span class="token punctuation">)</span>
</code></pre>
<p>De nuevo, una línea antes de la declaración de la función, agregamos el decorador…</p>
<pre class=" language-python"><code class="prism  language-python">@dispatch<span class="token punctuation">(</span><span class="token builtin">str</span><span class="token punctuation">,</span> <span class="token builtin">int</span><span class="token punctuation">,</span> <span class="token builtin">int</span><span class="token punctuation">)</span>
</code></pre>
<p>…con sus respectivos parámetros, para que la función correcta sea seleccionada en tiempo de ejecución.</p>
<h3 id="función-converter-completa-1">Función <code>converter</code> completa</h3>
<pre class=" language-python"><code class="prism  language-python">@dispatch<span class="token punctuation">(</span><span class="token builtin">str</span><span class="token punctuation">,</span> <span class="token builtin">int</span><span class="token punctuation">,</span> <span class="token builtin">int</span><span class="token punctuation">)</span>
<span class="token keyword">def</span>  <span class="token function">converter</span><span class="token punctuation">(</span>num<span class="token punctuation">:</span> <span class="token builtin">str</span><span class="token punctuation">,</span> from_base<span class="token punctuation">:</span> <span class="token builtin">int</span><span class="token punctuation">,</span> to_base<span class="token punctuation">:</span> <span class="token builtin">int</span><span class="token punctuation">)</span> <span class="token operator">-</span><span class="token operator">&gt;</span> <span class="token builtin">str</span><span class="token punctuation">:</span>
	<span class="token keyword">return</span> dec_to_base<span class="token punctuation">(</span>base_to_dec<span class="token punctuation">(</span>num<span class="token punctuation">,</span> from_base<span class="token punctuation">)</span><span class="token punctuation">,</span> to_base<span class="token punctuation">)</span>
</code></pre>
<h2 id="programa-completo">Programa Completo</h2>
<pre class=" language-python"><code class="prism  language-python"><span class="token keyword">from</span> functools <span class="token keyword">import</span> <span class="token builtin">reduce</span>
<span class="token keyword">from</span> multipledispatch <span class="token keyword">import</span> dispatch

equivalences <span class="token operator">=</span> <span class="token string">"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"</span>


<span class="token keyword">def</span> <span class="token function">dec_to_base</span><span class="token punctuation">(</span>num<span class="token punctuation">:</span> <span class="token builtin">int</span><span class="token punctuation">,</span> to_base<span class="token punctuation">:</span> <span class="token builtin">int</span><span class="token punctuation">)</span> <span class="token operator">-</span><span class="token operator">&gt;</span> <span class="token builtin">str</span><span class="token punctuation">:</span>
    valid_base<span class="token punctuation">(</span>to_base<span class="token punctuation">)</span>
    result <span class="token operator">=</span> <span class="token punctuation">[</span><span class="token punctuation">]</span>
    <span class="token keyword">while</span> num <span class="token operator">&gt;</span> <span class="token number">0</span><span class="token punctuation">:</span>
        calc <span class="token operator">=</span> num <span class="token operator">%</span> to_base
        result<span class="token punctuation">.</span>append<span class="token punctuation">(</span>equivalences<span class="token punctuation">[</span>calc<span class="token punctuation">]</span> <span class="token operator">or</span> calc<span class="token punctuation">)</span>
        num <span class="token operator">=</span> <span class="token builtin">int</span><span class="token punctuation">(</span>num <span class="token operator">/</span> to_base<span class="token punctuation">)</span>
    <span class="token keyword">return</span> <span class="token string">""</span><span class="token punctuation">.</span>join<span class="token punctuation">(</span>result<span class="token punctuation">.</span>__reversed__<span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">)</span>


<span class="token keyword">def</span> <span class="token function">base_to_dec</span><span class="token punctuation">(</span>num<span class="token punctuation">:</span> <span class="token builtin">str</span><span class="token punctuation">,</span> from_base<span class="token punctuation">:</span> <span class="token builtin">int</span><span class="token punctuation">)</span> <span class="token operator">-</span><span class="token operator">&gt;</span> <span class="token builtin">int</span><span class="token punctuation">:</span>
    valid_base<span class="token punctuation">(</span>from_base<span class="token punctuation">)</span>
    string_list <span class="token operator">=</span> <span class="token builtin">map</span><span class="token punctuation">(</span><span class="token keyword">lambda</span> x<span class="token punctuation">:</span> equivalences<span class="token punctuation">.</span>find<span class="token punctuation">(</span>x<span class="token punctuation">)</span><span class="token punctuation">,</span> num<span class="token punctuation">)</span>
    <span class="token keyword">return</span> <span class="token builtin">reduce</span><span class="token punctuation">(</span>
                    <span class="token keyword">lambda</span> acc<span class="token punctuation">,</span> curr<span class="token punctuation">:</span> acc <span class="token operator">+</span> curr<span class="token punctuation">[</span><span class="token number">1</span><span class="token punctuation">]</span> <span class="token operator">*</span> from_base <span class="token operator">**</span> <span class="token punctuation">(</span><span class="token builtin">len</span><span class="token punctuation">(</span>num<span class="token punctuation">)</span> <span class="token operator">-</span> curr<span class="token punctuation">[</span><span class="token number">0</span><span class="token punctuation">]</span> <span class="token operator">-</span> <span class="token number">1</span><span class="token punctuation">)</span><span class="token punctuation">,</span>
                    <span class="token builtin">enumerate</span><span class="token punctuation">(</span>string_list<span class="token punctuation">)</span><span class="token punctuation">,</span>
                    <span class="token number">0</span>
                <span class="token punctuation">)</span>


<span class="token keyword">def</span> <span class="token function">valid_base</span><span class="token punctuation">(</span><span class="token operator">*</span>bases<span class="token punctuation">:</span> <span class="token builtin">int</span><span class="token punctuation">)</span><span class="token punctuation">:</span>
    <span class="token keyword">for</span> base <span class="token keyword">in</span> bases<span class="token punctuation">:</span>
        <span class="token keyword">if</span> base <span class="token operator">&lt;</span> <span class="token number">2</span> <span class="token operator">or</span> base <span class="token operator">&gt;</span> <span class="token builtin">len</span><span class="token punctuation">(</span>equivalences<span class="token punctuation">)</span><span class="token punctuation">:</span>
            <span class="token keyword">raise</span> IndexError<span class="token punctuation">(</span>f<span class="token string">"Base must be higher or equal to 2 and lower or equal to {len(equivalences)}"</span><span class="token punctuation">)</span>

@dispatch<span class="token punctuation">(</span><span class="token builtin">int</span><span class="token punctuation">,</span> <span class="token builtin">int</span><span class="token punctuation">)</span>
<span class="token keyword">def</span> <span class="token function">converter</span><span class="token punctuation">(</span>num<span class="token punctuation">:</span> <span class="token builtin">int</span><span class="token punctuation">,</span> to_base<span class="token punctuation">:</span> <span class="token builtin">int</span><span class="token punctuation">)</span> <span class="token operator">-</span><span class="token operator">&gt;</span> <span class="token builtin">str</span><span class="token punctuation">:</span>
    <span class="token keyword">return</span> dec_to_base<span class="token punctuation">(</span>num<span class="token punctuation">,</span> to_base<span class="token punctuation">)</span>


@dispatch<span class="token punctuation">(</span><span class="token builtin">str</span><span class="token punctuation">,</span> <span class="token builtin">int</span><span class="token punctuation">,</span> <span class="token builtin">int</span><span class="token punctuation">)</span>
<span class="token keyword">def</span> <span class="token function">converter</span><span class="token punctuation">(</span>num<span class="token punctuation">:</span> <span class="token builtin">str</span><span class="token punctuation">,</span> from_base<span class="token punctuation">:</span> <span class="token builtin">int</span><span class="token punctuation">,</span> to_base<span class="token punctuation">:</span> <span class="token builtin">int</span><span class="token punctuation">)</span> <span class="token operator">-</span><span class="token operator">&gt;</span> <span class="token builtin">str</span><span class="token punctuation">:</span>
    <span class="token keyword">return</span> dec_to_base<span class="token punctuation">(</span>base_to_dec<span class="token punctuation">(</span>num<span class="token punctuation">,</span> from_base<span class="token punctuation">)</span><span class="token punctuation">,</span> to_base<span class="token punctuation">)</span>
</code></pre>
<br>	
<br>	
<br>	
<hr class="footnotes-sep">
<section class="footnotes">
<ol class="footnotes-list">
<li id="fn1" class="footnote-item"><p><a href="https://www.w3schools.com/python/python_lambda.asp">https://www.w3schools.com/python/python_lambda.asp</a>) <a href="#fnref1" class="footnote-backref">↩︎</a> <a href="#fnref1:1" class="footnote-backref">↩︎</a></p>
</li>
<li id="fn2" class="footnote-item"><p><a href="https://docs.python.org/3/library/functools.html#functools.reduce">https://docs.python.org/3/library/functools.html#functools.reduce</a> <a href="#fnref2" class="footnote-backref">↩︎</a></p>
</li>
<li id="fn3" class="footnote-item"><p><a href="https://www.w3schools.com/python/ref_func_enumerate.asp">https://www.w3schools.com/python/ref_func_enumerate.asp</a> <a href="#fnref3" class="footnote-backref">↩︎</a></p>
</li>
</ol>
</section>
</div>
</body>

</html>
