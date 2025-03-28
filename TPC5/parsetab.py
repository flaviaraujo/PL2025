
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "AJUDA CODIGO LISTAR MOEDA SAIR SELECIONAR VALOR_MOEDA\n    comando : ajuda\n            | listar\n            | moeda\n            | selecionar\n            | sair\n    ajuda : AJUDAlistar : LISTARmoeda : MOEDA lista_moedas '.' \n    lista_moedas : VALOR_MOEDA\n                | lista_moedas ',' VALOR_MOEDA\n    selecionar : SELECIONAR CODIGOsair : SAIR"
    
_lr_action_items = {'AJUDA':([0,],[7,]),'LISTAR':([0,],[8,]),'MOEDA':([0,],[9,]),'SELECIONAR':([0,],[10,]),'SAIR':([0,],[11,]),'$end':([1,2,3,4,5,6,7,8,11,14,15,],[0,-1,-2,-3,-4,-5,-6,-7,-12,-11,-8,]),'VALOR_MOEDA':([9,16,],[13,17,]),'CODIGO':([10,],[14,]),'.':([12,13,17,],[15,-9,-10,]),',':([12,13,17,],[16,-9,-10,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'comando':([0,],[1,]),'ajuda':([0,],[2,]),'listar':([0,],[3,]),'moeda':([0,],[4,]),'selecionar':([0,],[5,]),'sair':([0,],[6,]),'lista_moedas':([9,],[12,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> comando","S'",1,None,None,None),
  ('comando -> ajuda','comando',1,'p_comando','tpc5.py',89),
  ('comando -> listar','comando',1,'p_comando','tpc5.py',90),
  ('comando -> moeda','comando',1,'p_comando','tpc5.py',91),
  ('comando -> selecionar','comando',1,'p_comando','tpc5.py',92),
  ('comando -> sair','comando',1,'p_comando','tpc5.py',93),
  ('ajuda -> AJUDA','ajuda',1,'p_ajuda','tpc5.py',97),
  ('listar -> LISTAR','listar',1,'p_listar','tpc5.py',106),
  ('moeda -> MOEDA lista_moedas .','moeda',3,'p_moeda','tpc5.py',119),
  ('lista_moedas -> VALOR_MOEDA','lista_moedas',1,'p_lista_moedas','tpc5.py',124),
  ('lista_moedas -> lista_moedas , VALOR_MOEDA','lista_moedas',3,'p_lista_moedas','tpc5.py',125),
  ('selecionar -> SELECIONAR CODIGO','selecionar',2,'p_selecionar','tpc5.py',143),
  ('sair -> SAIR','sair',1,'p_sair','tpc5.py',159),
]
