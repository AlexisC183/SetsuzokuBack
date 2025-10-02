from django.shortcuts import render
from django.views import View

# Crea tus vistas aqui.

class PrincipalView(View):
    """Vista que renderiza el único archivo index.html de la aplicación."""

    def get(self, peticion):
        """Renderiza el xndex.html cuando se accede a la app vía URL, siempre y cuando la URL no coincida con la de otra vista."""

        return render(peticion, 'index.html')
