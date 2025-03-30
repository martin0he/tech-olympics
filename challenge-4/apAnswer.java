//question 4 answers

public Location getNextLoc(int row, int col) {
    Location under;
    int uVal;
    Location right;
    int rVal;
    for (int r = 0; r < grid.length; i++) {
        for (int c = 0; c < grid[0].length) {
            if (r == (row + 1) && c == col) {
                under = new Location(r, c);
                uVal = grid[r][c];
            }
            if (c == (col + 1) && r == row) {
                right = new Location(r, c);
                rVal = grid[c][r];
            }
        }
    }

    if (uVal > rVal) {
        return under;
    }
    else {
        return right;
    }
}

public int sumPath(int row, int col) {
    Location curr = getNextLoc(row, col);
    int sum = grid[row][col];
    while (curr.getRow() != grid.length - 1 && curr.getCol() != grid[0].length - 1) {
        sum += grid[curr.getRow()][curr.getCol()];
        curr = getNextLoc(curr.getRow(),curr.getCol());
    }
    sum += grid[curr.getRow()][curr.getCol()];
    return sum;
} 

********************************************************NEW VERSION:

public Location getNextLoc(int row, int col) {
    Location under = null;
    int uVal = Integer.MIN_VALUE;
    Location right = null;
    int rVal = Integer.MIN_VALUE;

    // Ensure we are within bounds
    if (row + 1 < grid.length) {  // Check if under is within bounds
        under = new Location(row + 1, col);
        uVal = grid[row + 1][col];
    }
    
    if (col + 1 < grid[0].length) {  // Check if right is within bounds
        right = new Location(row, col + 1);
        rVal = grid[row][col + 1];
    }

    // Choose the direction based on values, or fallback if one direction is out of bounds
    if (under != null && (right == null || uVal > rVal)) {
        return under;
    } else {
        return right;
    }
}

public int sumPath(int row, int col) {
    int sum = grid[row][col];
    Location curr = getNextLoc(row, col);
    
    while (curr != null && (curr.getRow() != grid.length - 1 || curr.getCol() != grid[0].length - 1)) {
        sum += grid[curr.getRow()][curr.getCol()];
        curr = getNextLoc(curr.getRow(), curr.getCol());
    }

    if (curr != null) {
        sum += grid[curr.getRow()][curr.getCol()];
    }
    
    return sum;
}
