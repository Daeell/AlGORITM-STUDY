def solution(brown, yellow):
    for width in range(3, int(brown/2)+1):
        height = (brown+4)//width
        if width*height-4 == brown+yellow:
            return [width, height]
    return []

    # for width in range(3, int((brown+4)/2)+1):
    #     height = (brown+4) // width -2
    #     if width * height - brown == yellow:
    #         return [width, height]
