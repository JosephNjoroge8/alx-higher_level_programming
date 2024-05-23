-- 16. Say my name
-- This script lists all records from 'second_table' with a non-NULL 'name', ordered by 'score' descending
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
