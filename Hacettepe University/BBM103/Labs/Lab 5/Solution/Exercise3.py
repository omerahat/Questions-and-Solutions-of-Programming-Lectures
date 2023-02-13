def towerofhanoi(n, source_rod, destination_rod, transfer_rod):
    if n > 0 and type(n)==int:
        towerofhanoi(n-1, source_rod, transfer_rod, destination_rod)
        print("Move disk", n, "from source", source_rod, "to destination", destination_rod)
        towerofhanoi(n-1, transfer_rod, destination_rod, source_rod)

towerofhanoi(int(input()),'A','C','B')