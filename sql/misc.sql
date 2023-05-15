SELECT
    DATE_TRUNC('month', activation_date) AS month,
    COUNT(CASE WHEN activation_date BETWEEN DATE_TRUNC('month', NOW()) AND NOW() THEN id END) AS activations_this_month,
    COUNT(CASE WHEN termination_date BETWEEN DATE_TRUNC('month', NOW()) AND NOW() THEN id END) AS terminations_this_month,
    COUNT(CASE WHEN activation_date BETWEEN DATE_TRUNC('month', DATE_SUB(NOW(), INTERVAL 1 MONTH)) AND DATE_SUB(NOW(), INTERVAL 1 MONTH) THEN id END) AS activations_last_month,
    COUNT(CASE WHEN termination_date BETWEEN DATE_TRUNC('month', DATE_SUB(NOW(), INTERVAL 1 MONTH)) AND DATE_SUB(NOW(), INTERVAL 1 MONTH) THEN id END) AS terminations_last_month
FROM
    customer_activation_termination
GROUP BY
    DATE_TRUNC('month', activation_date)
ORDER BY
    month DESC


SELECT
    DATE_TRUNC('month', activation_date) AS month,
    COUNT(CASE WHEN activation_date <= NOW() AND (termination_date > NOW() OR termination_date IS NULL) THEN id END) AS active_customers,
    COUNT(CASE WHEN YEAR(activation_date) = YEAR(NOW()) THEN id END) AS activations_ytd,
    COUNT(CASE WHEN YEAR(termination_date) = YEAR(NOW()) THEN id END) AS terminations_ytd
FROM
    customer_activation_termination
GROUP BY
    DATE_TRUNC('month', activation_date)
ORDER BY
    month DESC


SELECT DATE_TRUNC('month', '2023-05-14'::DATE) + INTERVAL '1 month' AS first_day_of_next_month;
