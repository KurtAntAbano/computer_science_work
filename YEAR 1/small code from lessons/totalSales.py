def total_sale(outlet1Sales, outlet2Sales, outlet3Sales):
    for i in range(0, 4):  # for each quarter
        total = 0
        for j in range(0, 3):
            total += outlet1Sales[i]
            total += outlet2Sales[i]
            total += outlet3Sales[i]
        print(f"Total for quarter {i + 1}: {total}")


total_sale([10, 12, 15, 10], [5, 8, 3, 6], [10, 12, 15, 10])


