replace = '''<div class="content-wrapper">
 <div class="text-border">
  <span class="icon-clothes mx-auto">
  </span>
  <div class="text text-center">
   Obecnie nie akceptujemy do sprzedaży męskie produkty podanej marki.
  </div>
 </div>
 <div class="text-md text-center">
  Możesz wysłać propozycję dodania marki.
 </div>
 <span class="text text-green hover-text-underline cursor-pointer d-inline-block">
  Wyślij propozycje
 </span>
</div>'''

with open("search_results_symbols.html", "r") as file:
    contents = file.read()
    contents = contents.replace(replace, "")

with open("search_results_symbols_clean.html", "w") as file:
    file.write(contents)