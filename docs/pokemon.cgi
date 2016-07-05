#!/usr/bin/perl

# magic - do not change
print "Content-type: text/html\n\n";
$page = $ENV{QUERY_STRING} || shift || 1;
# end magic

my $j = `joke`;

print <<EOF
<head>
<title>Pokemon</title>
</head>




<a href="about.html">Mangement</a>
|
<a href="game.html">Game corner</a>
|
<a href="http://lobberhead.com/">Lobberhead</a>
|
<a href="pokemon.html">Pokemon</a>
|
<a href="http://aple100.blogspot.com/">Blog</a>
|
<a href="games.html">Games</a>



<center>
<h1>Pokemom</h1>

</center>


<hr></hr>



<p>
<pre>
$j
</pre>
<p>


<img src="http://s1.hubimg.com/u/406796_f520.jpg" height=200>
<br>
click on the set you would like to buy from:








<p>
<p>
<p>



<center>
<a href="ex.html">

<img src="http://pokemonex.net/images/flame/logo.png"/>

<br>


<a href="ex.html">EX Pokemon Products</a>

</center>
<p>





<center>
<a href="dp.html">

<img src="http://www.supercheats.com/guides/files/guid/pokemon-diamond/logo.png"/>

<br>

<a href="dp.html">Dimond and Perl Products</a>
</center>




<center>

<a href="pl.html">

<img src="http://www.supercheats.com/guides/files/guid/pokemon-platinum/logo.png"/>

<br>

<a href="pl.html">Platunum Products</a>





</center>


<center>

<a href="hs.html">
<img src="http://cache.g4tv.com/ImageDb3/172435_S/Pokemon-HeartGold-And-SoulSilver-Coming-To-America-In-Spring-2010.jpg" height=200>
</a>

<br>


<a href="hs.html">Heartgold Soulsilver Products</a>

</center>



<p>

<center>
<a href="ul.html">
<img src="http://www.sixprizes.com/uploads/Unleashed-Logo-250x57.png"/>
</a>

<br>

<a href="ul.html">Unleashed Products</a>

<p>
<center>
<a href="un.html">
<img src="http://www.401games.ca/img/newrelease/pokemon_undaunted.jpg"/>
</a>

<br>

<a href="un.html">Undaunted Products</a>
</center>


<p>


<center>

<a href="other.html">Other Producs</a>

<hr></hr>

Copyright (C) David Skrenta 2010

<hr></hr>


</center>






























EOF
;


