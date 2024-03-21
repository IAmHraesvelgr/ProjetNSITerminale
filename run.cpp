#include <iostream>

/*
 * Ce fichier est le code source du programme d'installation et de lancement.
 * Pour plus de sécurité, l'utilisateur peut décider de le recompiler lui-même.
*/

#if _WIN32
  #include <windows.h>
  #define WINDOWS true
#endif

#if __unix 
  #define LINUX true
#endif

#if __APPLE__
  #define MACOS true
#endif

#define LOG(x) std::cout << x << std::endl

void install_windows_packages();
void install_unix_packages();

int main(int argc, char** argv)
{
  if (WINDOWS == true)
  {
    install_windows_packages();
  }
  else 
  {
    install_unix_packages();
  }

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

void install_unix_packages()
{
  if (system("python3 -m pip install --upgrade pip") == 0)
  {
    LOG("Pip a été mis à jour avec succès.");
  }
  else 
  {
    LOG("Erreur lors de la mise à jour de pip : vérifiez votre installation.");
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
