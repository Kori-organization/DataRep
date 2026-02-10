UPDATE report_card
SET final_situation =  
CASE 
    WHEN final_situation = 'true' THEN 'Aprovado'
    ELSE 'Reprovado'
END