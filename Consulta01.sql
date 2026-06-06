SELECT 
-- Classificação baseada nas palavras da base
    CASE 
        WHEN comentario LIKE '%excelente%' 
          OR comentario LIKE '%bom%' 
          OR comentario LIKE '%ótimo%' 
          OR comentario LIKE '%atencioso%' 
          OR comentario LIKE '%maravilhosa%' 
          OR comentario LIKE '%recomendo%' 
          OR comentario LIKE '%impecável%' 
          OR comentario LIKE '%adorei%' 
          OR comentario LIKE '%tranquilo%' 
          OR comentario LIKE '%rápido%' 
          OR comentario LIKE '%limpa%' 
          THEN 'Positivo'
          
        WHEN comentario LIKE '%ruim%' 
          OR comentario LIKE '%demora%' 
          OR comentario LIKE '%atraso%' 
          OR comentario LIKE '%atrasado%' 
          OR comentario LIKE '%inadmissível%' 
          OR comentario LIKE '%esperando%' 
          OR comentario LIKE '%travou%' 
          OR comentario LIKE '%falta de respeito%' 
          OR comentario LIKE '%péssima%' 
          OR comentario LIKE '%pressa%' 
          OR comentario LIKE '%problemas%' 
          THEN 'Negativo'
          
        ELSE 'Neutro/Outros'
    END AS sentimento_comentario,
    
-- 2. Conta quantos pacientes caíram em cada grupo
    COUNT(id_atendimento) AS total_comentarios

FROM historico_pacientes
WHERE comentario IS NOT NULL

-- 3. Agrupa e ordena para trazer o maior volume primeiro
GROUP BY sentimento_comentario
ORDER BY total_comentarios DESC;