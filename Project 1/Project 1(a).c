#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <math.h>
void merge(int n, int m, int arr[]);
void mergeSort(int lst[], int n, int m);
void insertionSort();
void hybridSort();
void randomArray();
void bestArray();
void worstArray();
#define INT_MAX 2147483647

int main(void) {

  // confirms that code is working as expected
  /*
  int arr[30];
  randomarray(30, arr);
  printf("Before: ");
  for (int i = 0; i < 30; i++){
    printf("%d ", arr[i]);
  }
  hybridSort(0, 29, arr, 0);
  // insertionSort(arr, 0, 29);
  printf("\n\nAfter: ");
  for (int j = 0; j < 30; j++){
    printf("%d ", arr[j]);
  }
  */
  
  FILE *f = fopen("results.csv", "w");
  fprintf(f, "n, best S, CPU time\n");
  
  srand(time(NULL));
  clock_t start, end; double cpu_time; 
  for (int n = 2; n <= pow(2, 18); n *= 2){ 
    double cpu_threshold = INT_MAX; int best_s = 1;
    
    for (int s = 2; s <= n; s *= 2){ 
      int *arr = malloc(n * sizeof(int));
      bestArray(n, arr); // to be toggled yourself
      start = clock();
      hybridSort(0, n-1, arr, s);
      end = clock();
      cpu_time = (double) ((end - start) * 1000000 / CLOCKS_PER_SEC); // multiplied for microseconds

      if (cpu_time < cpu_threshold){
        cpu_threshold = cpu_time;
        best_s = s;
      }
      free(arr);
    }
    printf("n = %d, best S = %d, CPU time = %f \n", n, best_s, cpu_threshold);
    fprintf(f, "%d, %d, %f\n", n, best_s, cpu_threshold);
    
  }
  fclose(f);
  
}

///////////// ARRAY MAKING ///////////////

void randomArray(int num, int *arr){
  srand(time(NULL));
  for (int i = 0; i < num; i++){
    arr[i] = rand() % 20000;
  }
}

void bestArray(int num, int *arr){
  for (int i = 0; i < num; i++){
    arr[i] = i;
  }
}

void worstArray(int num, int *arr){
  for (int i = 0; i < num; i++){
    arr[i] = num - i;
  }
}

///////////// METHODS ///////////////

void hybridSort(int n, int m, int *arr, int S){
  if (m - n <= 0) return;
  else if (m - n >= 1 && m - n + 1 <= S){ 
    insertionSort(arr, n, m);
  }
  else if (m - n >= 1 && m - n + 1 > S){
    int mid = (n + m)/2; 
    hybridSort(n, mid, arr, S);
    hybridSort(mid + 1, m, arr, S);
    merge(n, m, arr);
  }
}

void merge(int n, int m, int *arr){
  int mid = (n + m)/2;
  int len1 = mid - n + 1;
  int len2 = m - mid;

  int L[len1], R[len2];
  
  for (int i = 0; i < len1; i++){
    L[i] = arr[n + i];
  }
  for (int j = 0; j < len2; j++){
    R[j] = arr[mid + j + 1];
  }

  int ind = n, l = 0, r = 0;
  // printf("mergeSort \n");

  while (l < len1 && r < len2){
    if (L[l] < R[r]){
      arr[ind] = L[l];
      l++;
    }
    else {
      arr[ind] = R[r];
      r++;
    }
    ind++;
  }

  while (l < len1){
    arr[ind] = L[l];
    l++;
    ind++;
  }

  while (r < len2){
    arr[ind] = R[r];
    r++;
    ind++;
  }

}

void insertionSort(int *lst, int n, int m){

  if ((m - n) < 1) return;  

  int dummy;
  for (int i = n + 1; i < m + 1; i++){
    for (int j = i; j > n; j--){
      if (lst[j] < lst[j-1]){
        dummy = lst[j];
        lst[j] = lst[j-1];
        lst[j-1] = dummy;
      }
      else break;
    }
  }
}
