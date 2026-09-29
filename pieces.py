import pygame

class Piece:
    def __init__(self, pieceColour, pieceType, position):
        self.pieceColour = pieceColour
        self.pieceType = pieceType
        self.position = position
        self.legalMoves = []
    def findLegalMoves(self):
        pass
    def moveTo(self, newPosition):
        self.position = newPosition

class Pawn(Piece):
    def __init__(self, pieceColour, pieceType, position):
        super().__init__(pieceColour, pieceType, position)
        self.sprite = pygame.image.load(rf"sprites/pawn{pieceColour}2.png")

    def findLegalMoves(self):
        pass

class Rook(Piece):
    def __init__(self, pieceColour, pieceType, position):
        super().__init__(pieceColour,pieceType,position)
        self.sprite = pygame.image.load(rf"sprites/rook{pieceColour}2.png")

    def findLegalMoves(self):
        pass

class Bishop(Piece):
    def __init__(self, pieceColour, pieceType, position):
        super().__init__(pieceColour,pieceType,position)
        self.sprite = pygame.image.load(rf"sprites/bishop{pieceColour}2.png")

    def findLegalMoves(self):
        pass

class Knight(Piece):
    def __init__(self, pieceColour, pieceType, position):
        super().__init__(pieceColour, pieceType, position)
        self.sprite = pygame.image.load(rf"sprites/knight{pieceColour}2.png")

    def findLegalMoves(self):
        pass

class Queen(Piece):
    def __init__(self, pieceColour, pieceType, position):
        super().__init__(pieceColour, pieceType, position)
        self.sprite = pygame.image.load(rf"sprites/queen{pieceColour}2.png")

    def findLegalMoves(self):
        pass

class King(Piece):
    def __init__(self, pieceColour, pieceType, position):
        super().__init__(pieceColour, pieceType, position)
        self.sprite = pygame.image.load(rf"sprites/king{pieceColour}2.png")

    def findLegalMoves(self):
        pass