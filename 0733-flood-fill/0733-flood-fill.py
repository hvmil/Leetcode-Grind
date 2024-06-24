class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        original_color = image[sr][sc]

        def fill(image, sr, sc, original_color, new_color):
            if sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[0]) or image[sr][sc] != original_color:
                return

            image[sr][sc] = new_color

            fill(image, sr + 1, sc, original_color, new_color)
            fill(image, sr - 1, sc, original_color, new_color)
            fill(image, sr, sc + 1, original_color, new_color)
            fill(image, sr, sc - 1, original_color, new_color)

        fill(image, sr, sc, original_color, color)
        return image

        