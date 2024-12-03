# Знаходження найкоротшого шляху в лабіринті

### Організація роботи
Для зручної колаборації над програмою ми створили GitHub репозиторію для нашого проєкту. Під час першої особистої зустрічі ми вивчали разом наш основний алгоритм BFS, та декомпозували увесь проєкт на менші функції, а саме `read_file(filename: str) -> list[list[int | str]]`, `get_shortest_path(matrix: list[list[int | str]], start: tuple[int, int]) -> list[tuple[int, int]] | int`, `visualize_results(shortest_path: list[tuple[int, int]], matrix: list[list[int | str]]) -> str | None`, а також допоміжні функції: `find_start(matrix: list[list[int | str]]) -> tuple[int, int]`, `is_valid(matrix: list[list[int | str]], row: int, column: int) -> bool` (щоб перевіряти, чи клітина лабіринту є валідною для відвідування), `get_neighbors(matrix: list[list[int | str]], row: int, column: int) -> list[tuple[int, int]]`. Кінцевою стала розробка головної функції `main()`, що об’єднувала б увесь функціонал в єдину програму. Розподіливши завдання між собою ми виконували їх, підтримуючи зв’язок одне з одним, а також із Софією. Наша менторка швидко відповідала на наші запитання, та зрозуміло пояснювала вимоги до проєкту, даючи практичні поради щодо реалізації, за що ми їй вдячні.

### Візуалізація результатів: Unicode, ASCII та ANSI
Після успішної реалізації необхідного функціоналу та проміжного захисту ми з командою вирішили взятися за додаткові функції як-от візуалізація чи генерація випадкових лабіринтів. Візуалізація є важливою складовою для кращого розуміння результатів роботи алгоритму. Тому після розробки та тестування основного алгоритму з Мартою, я, Стратюк Арсеній, написав `visualize_results`. 
У процесі розробки функції я обрав використання Unicode-символів, зокрема емодзі, для створення візуалізації. Це рішення було прийнято після розгляду альтернатив, таких як ASCII-art та кольорові коди ANSI. Ось основні причини, плюси та мінуси цього підходу, а також опис роботи візуалізації.

#### Чому Unicode?  
1. **Чіткість і візуальна естетика:**  
   Unicode-символи, такі як 🟩, 🧱, 🚩 і 🏁, забезпечують інтуїтивно зрозуміле й привабливе уявлення елементів лабіринту.  
   - 🧱 — стіна  
   - 🟩 — шлях  
   - 🚩 — старт  
   - 🏁 — фініш  

2. **Глобальна підтримка:**  
   Unicode підтримується багатьма платформами, включаючи сучасні термінали, браузери й текстові редактори.

3. **Простота реалізації:**  
   Використання Unicode дозволяє уникнути складного управління кольорами (як у випадку з ANSI-кодами), оскільки кожен символ вже містить візуально розпізнавані елементи.

#### Порівняння з альтернативами  

| Підхід       | Переваги                                                                | Недоліки                                                                      |
|--------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| **Unicode**  | Чіткість, естетика, доступність, легка інтеграція.                      | Різні рендеринги символів на різних платформах. Використання більшого обсягу пам'яті. |
| **ASCII-art**| Висока сумісність, легкість у використанні для великих лабіринтів.      | Менш привабливий вигляд, відсутність кольорів.                                |
| **ANSI-коди**| Підтримка кольорів у терміналах. Сумісність з ASCII-art.                | Складність у читанні у файлах, несумісність із текстовими редакторами.        |

#### Особливості реалізації функції `visualize_results`

1. **Логіка роботи:**
   Функція `visualize_results` працює в кілька етапів. Спочатку вона проходить по всіх клітинах матриці лабіринту, перетворюючи кожну з них у відповідний символ за допомогою словника `cell_map`. Якщо клітина є частиною знайденого найкоротшого шляху, їй призначається символ 🟩, для старту використовується 🚩, для фінішу 🏁, а стіни й порожні клітини позначаються 🧱 та ⬜ відповідно. Отриманий візуалізований рядок додається до списку `visualizing_data`.  

   Після обробки всіх клітин лабіринту, створюється фінальний результат — стрічка, яка об'єднує всі рядки матриці. Для лабіринтів розміром до 31x31 ця стрічка повертається напряму для виведення в терміналі. Якщо ж лабіринт перевищує цей розмір, результат записується у файл у папці `Visualization`, де ім'я файлу вказує кількість кроків та розмір матриці. Такий підхід дозволяє зберігати високу читабельність для невеликих лабіринтів та ефективно працювати з великими структурами даних.

2. **Часова складність:**
   - Хоча основний алгоритм BFS працює за час O(V + E), візуалізація додає накладні витрати через ітерацію всієї матриці, що має складність O(n × m). Це призводить до уповільнення на великих матрицях (наприклад,      для розмірів понад 1000x1000). Через це ми додали можливість вимкнення візуалізації для тестування.

Вибір Unicode для візуалізації забезпечив високий рівень зручності, зрозумілості й візуальної естетики. Однак, це рішення має свої обмеження, зокрема, продуктивність і залежність від платформи. Тому можливість запису результатів у файл і відключення візуалізації є важливими елементами проєкту, що дозволяють працювати з великими даними ефективно. Загалом візуалізація значно підвищила цінність нашого проєкту, зробивши його зрозумілішим та зручнішим для користувача.

### Input
- A matrix of size `n x m` (where `1 ≤ n, m ≤ 10^4`), provided in a `.csv` file.
- The matrix format:
  - `0` represents walkable paths.
  - `1` represents walls.
  - `S` represents the start position.
  - `E` represents the end position.

### Output
- An array of tuples `[(a, b), ...]` representing the shortest path from the start to the endpoint.
- Returns `-1` if no path exists.

### Algorithm
The project uses the **Breadth-First Search (BFS)** algorithm for its efficiency in finding the shortest path in an unweighted graph. BFS ensures optimal performance even for large matrices.

---

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/ArseniiStratiuk/Maze-Shortest-Path.git
   ```

---

## Code Architecture

### Modules and Functions

#### `read_file(filename: str) -> list[list[int | str]]`
- Reads and parses the `.csv` input file, returning a 2D list representation of the maze.
- **To-Do:** Add help messages for argparse commands.

#### `find_start(filename: str) -> tuple[int, int]`
- Identifies the start position (`S`) in the maze.

#### `get_neighbors(matrix: list[tuple[int, int]], row: int, column: int) -> list[tuple[int, int]]`
- Returns valid neighboring cells for a given cell in the maze.

#### `is_valid() -> bool`
- Validates maze cell.

#### `get_shortest_path(matrix: list[tuple[int, int]], finish: tuple[int, int], start: tuple[int, int]) -> list[tuple[int, int]] | int`
- Implements the **BFS** algorithm to find the shortest path.
- **To-Do:** Add tests, optimize.

#### `visualize_results(shortest_path: list[tuple[int, int]], matrix: list[tuple[int, int]])`
- Visualizes the shortest path on the maze.
- **To-Do:** Develop visualization logic using ASCII art or libraries like `matplotlib`.

---

## To-Do List

1. **Performance Optimization:**
   - Investigate the use of deque for BFS to optimize queue operations.

2. **Visualization:**
   - Implement the `visualize_results` function to understand the output path better.

3. **Documentation:**
   - Add detailed docstrings for all functions.
   - Include a diagram or flowchart for the BFS algorithm.
