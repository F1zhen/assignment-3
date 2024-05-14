public class InsertionSort {
    public void insertionSort(int[] arr) {
        int n = arr.length;

        if (n <= 1) {
            return;
        }

        for (int i = 1; i < n; i++) {
            int key = arr[i];
            int j = i - 1;
            while (j >= 0 && key < arr[j]) {
                arr[j + 1] = arr[j];
                j -= 1;
            }
            arr[j + 1] = key;
        }
    }
}