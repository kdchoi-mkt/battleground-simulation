# Hearthstone Battleground Simulation
하스스톤 전장 시뮬레이션을 만들고 있습니다

## Objective
1. 직관적으로 좋다고 하는 하수인(기물)이 정말로 좋을까?
2. 더 나아가서, 사람들이 하고 있는 선택은 최적의 선택인가?

이러한 질문에 답을 하기 위해서 각 기물 별로 전투 시뮬레이션을 만들고 있습니다

## End Image
1. 각 턴, 각 선술집 레벨마다 성능이 좋은 하수인 순으로 Ranking
2. 각 턴에 가장 좋은 조합을 찾기

## Why Simulation?
+ 전장에서 일어나는 모든 움직임들은 Discrete Choice이기 때문에 유한한 경우의 수 내에서 일어납니다
+ 그러나 각자가 선택할 수 있는 환경이 너무 방대하기 때문에, simulation이라는 툴을 통해서 확률을 근사하고자 합니다

# To Do

# Git Description
## Board
+ `Player`: 플레이어에 대한 객체가 저장되어있습니다
+ `Shop`: 선술집에 대한 객체가 저장되어있습니다
## Card
+ `Card`: 카드에 대한 객체가 저장되어있습니다
  1. 현재 황금 카드는 객체를 만들지 않았으며
  2. 대부분의 카드가 형태만 존재합니다
  
## Example
+ `SimulationExample{X}`: 시뮬레이션이 잘 작동하는지 파악하기 위해 만든 Mock Data입니다. 실제 전장 전투 기반으로 만들어졌으며, 출처는 주석으로 달아놓았습니다

## Minion Generator
+ `ExtractInfo`: HTML 코드에서 각 카드의 정보를 JSON 형태로 가져옵니다 (Resource의 html코드를 이용하여 위의 객체를 모두 만들었으며, 출처는 나무위키입니다)
+ `MinionGenerator`: `ExtractInfo`에서 가져온 JSON을 토대로 각 기물 별 객체를 python 파일로 구성합니다
+ `MinionGroupAppender`: `MinionGenerator`가 끝난 후, 각 종족 별로 기물을 묶을 수 있게 종족 별 `minion_group`을 `__init__.py`에 저장합니다
+ `ResetCardInfo`: 중간에 놓친 부분이 있거나 코드가 꼬인 부분이 있을 때, 지금까지 만들었던 모든 코드를 리셋합니다. (웬만하면 쓰지 않는게 좋습니다.)

## Resources
+ `Tier{X}`: 하스스톤 전장 X티어에 대한 HTML source입니다 (출처는 나무위키입니다)

## Automatically Generated Examplar
1. 각 레벨, 각 티어에 따라서 생성될 수 있는 필드의 가짓수를 Automatically하게 만드는 것이 목표입니다
2. 다만, 전장에는
  + `전투의 함성 (Battle Cry)`, `혈석 (Blood Stone)` 등의 업그레이드 요소 및
  + 서로 다른 `영응 능력 (Hero Power)`
  + 그리고 전투 중에 영구적으로 버프를 부여하는 하수인이 있어서 Pure Randomize를 통한 Ability 생성은 이치에 맞지 않습니다
3. 따라서, 전투의 함성, 혈석 및 영웅 능력 등을 적절히 부여하는 알고리즘을 작성하여 각 턴에 알맞는 필드를 생성하는 것이 최종 목표입니다
4. 첫 번째 To Do가 끝나면, 각 턴마다 적어도 100가지가 넘는 예시들이 만들어질 예정입니다 

## Measure the Performance
1. 위의 예시들을 기반으로 기물의 평균 퍼포먼스를 측정할 수 있습니다
2. 동일 조건에서 기물만 서로 변경하면서, 전투에서 승리할 확률을 체크합니다
3. 각각 조건에 따라 Linear Regression, 혹은 Causal Tree Analysis 등을 통해서 각 기물의 능력치를 측정합니다
