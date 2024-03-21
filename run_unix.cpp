#include <iostream>

/*
 * Ce fichier est le code source du programme d'installation et de lancement.
 * Pour plus de sécurité, l'utilisateur peut décider de le recompiler lui-même.
*/

#define LOG(x) std::cout << x << std::endl;

void install_unix_packages();

int main(int argc, char** argv)
{
  install_unix_packages();
  return 0;
}

void install_unix_packages()
{
  if (system("python3 -m pip install --upgrade pip") == 0)
  {
    LOG("Pip 3 a été mis à jour avec succès.");
  }
  else 
  {
    LOG("Erreur lors de la mise à jour de pip 3 : vérifiez votre installation.");
    exit(-1);
  }

  if (system("python3 -m pip install -r ./resources/requierments.txt") == 0)
  {
    LOG("Les dépendances ont été installées avec succès.");
  }
  else 
  {
    LOG("Erreur lors de l'installation des dépendances : vérifiez votre installation.");
    exit(-1);
  }
  
  if (system("python3 ./src/main.py") == 0)
  {
    LOG("Programme exécuté avec succès.");
  }
  else 
  {
    LOG("Erreur lors de l'exécution du programme");
    exit(-1);
  }
}
