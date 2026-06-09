int NaiveFactoring(int n){
      for(int i = 2; i * i <= n; i++){
          if(n % i == 0)  return i;
      }
      return 0; //Not found.
}