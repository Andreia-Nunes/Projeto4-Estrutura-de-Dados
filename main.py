import random
import time
import algoritmos

# --------------------- Construindo vetor com números aleatórios ---------------------

vetorOriginal = []

for i in range(0, 20000):
    vetorOriginal.append(random.randint(1, 5000))


# ----------------------- Realizando cópias do vetor original ------------------------

vetorBubble = vetorOriginal.copy()
vetorInsertion = vetorOriginal.copy()
vetorShell = vetorOriginal.copy()
vetorQuick = vetorOriginal.copy()
vetorMerge = vetorOriginal.copy()

print(f"\nRESULTADOS:")
print()


# ------------------------------- Testando Bubble Sort -------------------------------

inicialTime = time.time()
algoritmos.bubbleSort(vetorBubble)
finalTime = time.time()

tempoBubble = finalTime - inicialTime
print(f"Bubble Sort: {tempoBubble:.5f} seg")


# ------------------------------ Testando Insertion Sort -----------------------------

inicialTime = time.time()
algoritmos.insertionSort(vetorInsertion)
finalTime = time.time()

tempoInsertion = finalTime - inicialTime
print(f"Insertion Sort: {tempoInsertion:.5f} seg")


# -------------------------------- Testando Shell Sort -------------------------------

inicialTime = time.time()
algoritmos.shellSort(vetorShell)
finalTime = time.time()

tempoShell = finalTime - inicialTime
print(f"Shell Sort: {tempoShell:.5f} seg")


# -------------------------------- Testando Merge Sort -------------------------------

inicialTime = time.time()
algoritmos.mergeSort(vetorMerge)
finalTime = time.time()

tempoMerge = finalTime - inicialTime
print(f"Merge Sort: {tempoMerge:.5f} seg")


# -------------------------------- Testando Quick Sort -------------------------------

inicialTime = time.time()
algoritmos.quickSort(vetorQuick, 0, len(vetorQuick) - 1)
finalTime = time.time()

tempoQuick = finalTime - inicialTime
print(f"Quick Sort: {tempoQuick:.5f} seg")



