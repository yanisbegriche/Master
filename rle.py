#include <stdio.h>
#include <string.h>
#include <stdlib.h>
//#include <compress.h>

/** RLE decompress  function **/
char *decompress(const char *str, unsigned char base)
{
      char *result =  (char*)calloc(strlen(str), sizeof(char));
      char *tmp =  (char*)calloc(strlen(str), sizeof(char));
      char fmt[10];
      char tmp2[10];
      char ch ;
      int n = strlen(str) ;
      
      switch (base) {
           case 8:
               sprintf(fmt,"%s","%o");
                break;
           case 10:
               sprintf(fmt,"%s","%d");
                break;
           case 16:
               sprintf(fmt,"%s","%x");
                break;
        }
          
      
      int i = 0;
      strcpy(result,"");
      
      while  (i < n ) {
         strcpy(tmp,"");
         strcpy(tmp2,"");
         ch = str[i];
         int nb=0;
         int tot=sscanf(&ch, fmt, &nb) ;     

         ch = str[++i];
         for (int k=1; k<=nb; k++) {
             sprintf(tmp2,"%c",ch);
             strcat(tmp,tmp2);      
       }
         
         strcat(result,tmp) ;
         i++ ;
      }
      
      
return result;
}

/** RLE Compress  function **/
char *compress(const char *str, unsigned char base)
{

      char *result =  (char*)calloc(strlen(str), sizeof(char));
      int n = strlen(str) ;
      char tmp[n];
      char tmp2[n];
      char fmt[10];
//      int ibase=(uint)base;
      if(n == 0)     {
        strcpy(result,"");
        return result;
      }

      switch (base) {
           case 8:
               sprintf(fmt,"%s","%o%c");
                break;
           case 10:
               sprintf(fmt,"%s","%d%c");
                break;
           case 16:
               sprintf(fmt,"%s","%X%c");
                break;
        }
               
    int count = 1;
    for(int i = 0; i < n; i++)
    {
        while(str[i] == str[i+1]) {
            count++;
            i++;
        }

        int c = count/(base-1); 
        int r = count%(base-1);
        strcpy(tmp2, "");
        strcpy(tmp, "");
        for(int k=0; k<c; k++){
            sprintf(tmp2,fmt,base-1,str[i]);
            strcpy(tmp,tmp2);
        }
        if (r >0) {
           strcpy(tmp2, "");
           sprintf(tmp2,fmt,r,str[i]);
           strcat(tmp,tmp2);
        }

        strcat(result,tmp);
        count = 1;
    }
    return result;

}

int main()
{

char *strcompres ;
char *destrcompres ;
char str[20] ;

strcpy(str, "abGGGGGGGGGG");
//strcompres = compress("aaaaaaaab", 8);
//strcompres = compress("9999999999",16);
strcompres = compress(str,10);
printf("compress of %s is :  %s  \n",str, strcompres);

//destrcompres = decompress("7a1a1b",8);
//destrcompres = decompress("A9",16);
destrcompres = decompress(strcompres,10);
printf("destrcompres of %s is : %s  \n",strcompres, destrcompres);
return 0;
}

