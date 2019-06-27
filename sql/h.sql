SELECT *
FROM SIMPLE s
WHERE s.CREATOR.NAME = 'Matheus' AND ((trunc(sysdate) - (trunc(sysdate)+s.DURATION) < 0) or s.CONCLUSION_DATE IS NOT NULL);