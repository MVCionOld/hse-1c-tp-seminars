**Замечание 1:**  
Двоеточие после условия (в конце строки if) обязательно!

**Замечание 2:**  
После if и после else!

**Замечание 3:**  
В Python группы команд определяются *ОТСТУПАМИ*! За отступами нужно *ВНИМАТЕЛЬНО* следить! Отступами могут служить и пробелы, и знаки табуляции, но ни в коем случае не перемешивайте их! Как правило, в качестве отступа используют 4 пробела, но иногда можно встретить исходники с 2 или 8 символами пробела. Использование знаков табуляции является плохой практикой и следует избегать их (не только в Python: [прочитайте](https://habr.com/ru/post/331026/)).

**Замечание 4:**  
В Python нет операторных скобок, в отличие от таких языков, как С++ или Java. В этих языках набор команд, которые должны быть выполнены при определённом условии, определяется расположением скобок, например что-то вроде:
```
if (<condition>) {
  <cmd1>;
  ...
  <cmdN>;
} else {
  <cmdM>;
}
```
Здесь команды <cmd1> ... <cmd1> выполняются внутри блока с истинным <condition>, иначе выполняется <cmdM>.

На Python это выглядит вот так:
```
if <condition>:
    <cmd1>
    ...
    <cmdN>
else:
    <cmdM>
```