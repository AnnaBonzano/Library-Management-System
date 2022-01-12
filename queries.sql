
/* Q1 */
SELECT COUNT(*) AS "Number of Copies"
FROM ItemCopy
WHERE itemID = "6565";

/* Q2 */
SELECT p.patronID, p.cardID, p.fName, p.lName, f.fineAmount
FROM Patron p, Fine f
WHERE p.patronID = f.patronID AND f.fineAmount > 0;

/* Q3 */
SELECT p.cardID, SUM(f.fineAmount) AS "Total Fines"
FROM Patron p, Fine f
WHERE p.patronID = f.patronID
GROUP BY p.cardID;

/* Q4 */
SELECT f.patronID, f.fineID, f.damage, f.dateIssued, SUM(f.fineAmount) AS "Amount Owed"
FROM Fine f
GROUP BY f.patronID, f.fineID, f.damage, f.dateIssued
ORDER BY f.patronID, f.fineID, f.damage, f.dateIssued;

/* Q5 */
SELECT ic.copyID, ic.itemID, ic.categoryID, (DATEDIFF (r.expectedReturn, r.dateLoaned) - icat.checkoutPeriod) AS "Overdue"
FROM ItemCopy ic, Request r, ItemCategory icat
WHERE ic.categoryID = icat.categoryID AND ic.itemID = r.itemID AND icat.checkoutPeriod < DATEDIFF(r.expectedReturn, r.dateLoaned);

/* Q6 */
/*considering today is 2020-05-15*/
SELECT *
FROM Request
WHERE dateLoaned > "2020-05-15";

/* Q7 */
SELECT SUM(fineAmount) AS "Total Revenue"
FROM Fine;

/* Q8 */
SELECT categoryID, categoryName, maxRenewals, checkoutPeriod AS "Max. of Checkout Days"
FROM ItemCategory;

/* Q9 */
SELECT r.patronID, r.requestID, r.dateLoaned, i.itemName, i.type, COUNT(r.itemID) AS "No. of Items"
FROM Request r, Item i
WHERE r.itemID = i.itemID
GROUP BY r.patronID, r.requestID, r.dateLoaned, i.itemName, i.type;

/* Q10 */
INSERT INTO Request
VALUES ('54982','2000','2839','2020-07-10','2020-07-16');




