def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Cek baris, kolom, dan diagonal
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def get_move():
    while True:
        try:
            move = int(input("Masukkan nomor posisi (1-9): "))
            if move in range(1, 10):
                return move
            else:
                print("Nomor posisi harus antara 1 dan 9.")
        except ValueError:
            print("Input tidak valid. Masukkan nomor posisi antara 1 dan 9.")

def is_board_full(board):
    return all(all(cell != " " for cell in row) for row in board)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    print("Selamat datang di permainan Tic-Tac-Toe!")
    print_board(board)

    while True:
        print(f"Giliran pemain {players[current_player]}")
        move = get_move() - 1
        row, col = divmod(move, 3)

        if board[row][col] != " ":
            print("Posisi sudah ditempati. Coba lagi.")
            continue

        board[row][col] = players[current_player]
        print_board(board)

        if check_winner(board, players[current_player]):
            print(f"Pemain {players[current_player]} menang!")
            break

        if is_board_full(board):
            print("Permainan seri!")
            break

        current_player = 1 - current_player

if __name__ == "__main__":
    main()
      
