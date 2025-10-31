-- 코드를 작성해주세요
SELECT E.EMP_NO, E.EMP_NAME,
    CASE
        -- 위에서부터 구간을 검사하며 내려옴
        WHEN G.AVG_SCORE >= 96 THEN 'S'     
        WHEN G.AVG_SCORE >= 90 THEN 'A'
        WHEN G.AVG_SCORE >= 80 THEN 'B'
        ELSE 'C'
    END AS GRADE,
    CASE
        WHEN G.AVG_SCORE >= 96 THEN ROUND(E.SAL * 0.20)
        WHEN G.AVG_SCORE >= 90 THEN ROUND(E.SAL * 0.15)
        WHEN G.AVG_SCORE >= 80 THEN ROUND(E.SAL * 0.10)
        ELSE 0
    END AS BONUS
FROM HR_EMPLOYEES E
JOIN (
    -- 2022년의 각 사원별 평균 등급 계산
    SELECT EMP_NO, AVG(SCORE) AS AVG_SCORE
    FROM HR_GRADE
    GROUP BY EMP_NO     
) AS G
ON E.EMP_NO = G.EMP_NO
ORDER BY E.EMP_NO ASC;