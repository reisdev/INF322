/* Criar categoria */
INSERT INTO CATEGORIES (NAME,DESCRIPTION)
    VALUES('Aviação','Produtos que te levem às Alturas')
/

/* Criar um novo item */
INSERT INTO ITEM (NAME,DESCRIPTION,CATEGORY)
    VALUES('Propulsor', 'Um propulsor de 900J de força',(SELECT REF(c) FROM CATEGORIES c WHERE c.NAME='Aviação'));
/

/* Inserir uma nova venda simples */
INSERT INTO SIMPLE (ID,ITEM,CREATOR,PRICE,DURATION,POST_DATE,QUANTITY)
VALUES((SELECT COUNT(1) FROM SIMPLE),(SELECT REF(i) FROM ITEM i WHERE i.NAME = 'Propulsor'),(SELECT REF(u) FROM USERS u WHERE u.NAME = 'Matheus'),2000,30,systimestamp,2);
/

/* Prorrogar a Duração */
UPDATE SIMPLE
SET DURATION = 45
WHERE ID=0;

/* Dar baixa no anúncio */
UPDATE SIMPLE
SET CONCLUSION_DATE = DATE'2019-06-28'
WHERE ID=0;
/