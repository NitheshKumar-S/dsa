# Determine if a 9x9 Sudoku board is valid.

# Rules:
# - Each row must have digits 1-9 with no repeats
# - Each column must have digits 1-9 with no repeats
# - Each of the nine 3x3 sub-boxes must have no repeats
# - Empty cells contain '.'

# What do we need to track?
# - Which numbers appeared in each row (9 rows)
# - Which numbers appeared in each column (9 cols)
# - Which numbers appeared in each 3x3 box (9 boxes)

# Key insight for box index:
# box_index = (row // 3) * 3 + (col // 3)

# Row 0-2, Col 0-2 → box 0
# Row 0-2, Col 3-5 → box 1
# Row 0-2, Col 6-8 → box 2
# Row 3-5, Col 0-2 → box 3
# ... and so on

def isValidSudoku(board):
    # Use sets to track seen numbers
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    
    for r in range(9):
        for c in range(9):
            val = board[r][c]
            
            # Skip empty cells
            if val == '.':
                continue
            
            # Calculate box index
            box_idx = (r // 3) * 3 + (c // 3)
            
            # Check if already seen
            if (val in rows[r] or
                val in cols[c] or
                val in boxes[box_idx]):
                return False
            
            # Mark as seen
            rows[r].add(val)
            cols[c].add(val)
            boxes[box_idx].add(val)
    
    return True

# Time: O(81) = O(1) fixed board size
# Space: O(81) = O(1) fixed