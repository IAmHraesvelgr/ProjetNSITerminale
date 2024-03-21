#include <iostream>
#include <windows.h>

/*
 * Ce fichier est le code source du programme d'installation et de lancement.
 * Pour plus de sécurité, l'utilisateur peut décider de le recompiler lui-même.
*/

#define LOG(x) std::cout << x << std::endl;

void install_windows_packages();

int main(int argc, char** argv)
{
  install_windows_packages();
  return 0;
}

void install_windows_packages()
{
  SetConsoleOutputCP(CP_UTF8);
  if (system("pip install --upgrade pip") == 0)
  {
    LOG("Pip a été mis à jour avec succès.");
  }
  else 
  {
    LOG("Erreur lors de la mise à jour de pip : vérifiez votre installation.");
    exit(-1);
  }

  if (system("pip install -r ./resources/requierments.txt") == 0)
  {
    LOG("Les dépendances ont été installées avec succès.");
  }
  else 
  {
    LOG("Erreur lors de l'installation des dépendances : vérifiez votre installation.");
    exit(-1);
  }

  if (system("python ./src/main.py") == 0)
  {
    LOG("Programme exécuté avec succès.");
  }
  else 
  {
    LOG("Erreur lors de l'exécution du programme");
    exit(-1);
  }
}
