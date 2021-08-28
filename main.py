#include<stdio.h>
int main()
{
    
  double marksInphysics,marksInmaths,marksIncprogram,marksInenglish;
  marksInphysics=78.00;
  marksInmaths=65.00;
  marksIncprogram=67.00;
  marksInenglish=45.00;
  avarage=(marksInphysics+marksInmaths+marksIncprogram+marksInenglish)/4;
  
  printf("%.21f\n",avarage);
  return 0;
}
