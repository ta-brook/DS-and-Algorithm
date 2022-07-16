/*
Each node in the tree can be one of three types:
    "Leaf": if the node is a leaf node.
    "Root": if the node is the root of the tree.
    "Inner": If the node is neither a leaf node nor a root node.

Write an SQL query to report the type of each node in the tree.
*/

SELECT
    id, 
    'Root' AS type
FROM 
    Tree
WHERE
    p_id IS NULL
    
UNION

SELECT
    id,
    'Leaf' as type
FROM
    Tree
WHERE
    id NOT IN (
        SELECT 
            DISTINCT p_id
        FROM
            Tree
        WHERE
            p_id IS NOT NULL
    )
    AND
    p_id IS NOT NULL

UNION

SELECT
    id,
    'Inner' AS Type
FROM
    Tree
WHERE
    id IN (
        SELECT 
            DISTINCT p_id
        FROM
            Tree
        WHERE
            p_id IS NOT NULL
    )
    AND
    p_id IS NOT NULL
    
ORDER BY id

/*
Input: 
Tree table:
+----+------+
| id | p_id |
+----+------+
| 1  | null |
| 2  | 1    |
| 3  | 1    |
| 4  | 2    |
| 5  | 2    |
+----+------+
Output: 
+----+-------+
| id | type  |
+----+-------+
| 1  | Root  |
| 2  | Inner |
| 3  | Leaf  |
| 4  | Leaf  |
| 5  | Leaf  |
+----+-------+
Explanation: 
Node 1 is the root node because its parent node is null and it has child nodes 2 and 3.
Node 2 is an inner node because it has parent node 1 and child node 4 and 5.
*/

/*
Input: 
Tree table:
+----+------+
| id | p_id |
+----+------+
| 1  | null |
+----+------+
Output: 
+----+-------+
| id | type  |
+----+-------+
| 1  | Root  |
+----+-------+
Explanation: If there is only one node on the tree, you only need to output its root attributes.
*/