
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '\xb7c\xad$Hg+\x85lDW\xed\xfaJ|;'
    
_lr_action_items = {'TYPEID':([0,1,3,5,7,10,11,12,13,14,20,28,30,31,32,38,97,112,],[2,-3,-6,-5,2,16,-45,-4,16,16,16,-12,-11,-7,-13,16,16,-36,]),'LBRACE':([4,37,76,],[10,-46,97,]),'RPAREN':([13,24,25,26,29,35,38,42,48,49,50,51,52,55,56,57,58,68,72,73,74,77,78,79,80,81,83,84,90,91,92,93,94,95,96,100,101,102,103,104,105,107,108,109,110,111,],[-51,37,-49,-48,-47,-51,-51,-28,-41,-40,-39,-38,75,-27,-28,76,-50,-33,-51,-51,-51,-30,-29,-31,-19,-18,-27,-20,105,-22,-21,-32,-44,-43,-42,107,108,109,110,111,-35,-25,-26,-23,-24,-34,]),'RBRACE':([10,14,18,20,22,27,28,30,32,33,97,106,112,],[-51,-51,31,-51,-8,-9,-12,-11,-13,-10,-51,112,-36,]),'SEMI':([4,15,17,19,29,37,39,40,41,42,45,46,47,55,56,68,75,77,78,79,80,81,83,84,91,92,93,105,107,108,109,110,111,],[11,28,30,32,-47,-46,-15,-16,-18,-28,-14,-27,-17,-27,-28,-33,-37,-30,-29,-31,-19,-18,-27,-20,-22,-21,-32,-35,-25,-26,-23,-24,-34,]),'MINUS':([42,46,64,65,83,98,99,],[63,69,86,88,69,86,88,]),'EQUALS':([21,],[34,]),'SCONST':([35,72,73,74,],[48,48,48,48,]),'PLUS':([42,46,64,65,83,98,99,],[62,70,85,87,70,85,87,]),'LT':([41,42,46,54,55,56,64,65,],[59,-28,-27,59,-27,-28,-27,-28,]),'GT':([41,42,46,54,55,56,64,65,],[60,-28,-27,60,-27,-28,-27,-28,]),'COMMA':([25,29,48,49,50,],[38,-47,72,73,74,]),'LPAREN':([9,21,23,34,36,43,44,46,53,62,63,67,69,70,71,85,86,87,88,89,],[13,35,36,43,53,53,67,35,53,82,82,53,82,82,53,82,82,82,82,53,]),'OR':([47,55,56,57,66,68,77,78,79,90,93,104,105,111,],[71,-27,-28,71,89,71,-30,-29,-31,89,71,71,-35,-34,]),'NOT':([34,36,43,44,53,67,71,89,],[44,44,44,44,44,44,44,44,]),'ICONST':([34,35,36,43,44,53,59,60,61,62,63,67,69,70,71,72,73,74,82,85,86,87,88,89,],[42,49,56,65,56,56,56,56,56,42,42,56,42,42,56,49,49,49,99,42,42,42,42,56,]),'IF':([10,14,20,28,30,32,97,112,],[23,23,23,-12,-11,-13,23,-36,]),'EQ':([41,42,46,54,55,56,64,65,],[61,-28,-27,61,-27,-28,-27,-28,]),'ID':([2,10,14,16,20,28,30,32,34,35,36,43,44,53,59,60,61,62,63,67,69,70,71,72,73,74,82,85,86,87,88,89,97,112,],[9,21,21,29,21,-12,-11,-13,46,50,55,64,55,55,55,55,55,83,83,55,83,83,55,50,50,50,98,83,83,83,83,55,21,-36,]),'$end':([0,1,3,5,6,7,8,11,12,31,],[-51,-3,-6,-5,0,-1,-2,-45,-4,-7,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'external_declaration':([0,7,],[1,12,]),'expression_statement':([10,14,20,97,],[14,14,14,14,]),'cond_expression':([34,36,43,44,53,67,71,89,],[47,57,66,68,66,90,93,104,]),'function_definition':([0,7,],[3,3,]),'func_decl':([0,7,],[4,4,]),'function_declaration':([0,7,],[5,5,]),'unary_expression':([34,36,43,44,53,59,60,61,62,63,67,69,70,71,85,86,87,88,89,],[41,54,54,54,54,77,78,79,81,81,54,81,81,54,81,81,81,81,54,]),'param_list':([13,38,],[24,58,]),'assignment_statement':([10,14,20,97,],[17,17,17,17,]),'func_call':([10,14,20,34,97,],[15,15,15,39,15,]),'translation_unit_or_empty':([0,],[6,]),'translation_unit':([0,],[7,]),'statement':([10,14,20,97,],[18,27,33,106,]),'declarator':([10,13,14,20,38,97,],[19,25,19,19,25,19,]),'if_statement':([10,14,20,97,],[20,20,20,20,]),'expression':([34,],[45,]),'arg_list':([35,72,73,74,],[52,94,95,96,]),'empty':([0,10,13,14,20,35,38,72,73,74,97,],[8,22,26,22,22,51,26,51,51,51,22,]),'binary_expression':([34,62,63,69,70,85,86,87,88,],[40,80,84,91,92,100,101,102,103,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> translation_unit_or_empty","S'",1,None,None,None),
  ('translation_unit_or_empty -> translation_unit','translation_unit_or_empty',1,'p_translation_unit_or_empty','lexer.py',82),
  ('translation_unit_or_empty -> empty','translation_unit_or_empty',1,'p_translation_unit_or_empty','lexer.py',83),
  ('translation_unit -> external_declaration','translation_unit',1,'p_translation_unit_1','lexer.py',88),
  ('translation_unit -> translation_unit external_declaration','translation_unit',2,'p_translation_unit_2','lexer.py',93),
  ('external_declaration -> function_declaration','external_declaration',1,'p_external_declaration_1','lexer.py',98),
  ('external_declaration -> function_definition','external_declaration',1,'p_external_declaration_2','lexer.py',103),
  ('function_definition -> func_decl LBRACE statement RBRACE','function_definition',4,'p_function_definition','lexer.py',108),
  ('statement -> empty','statement',1,'p_statement','lexer.py',113),
  ('statement -> expression_statement statement','statement',2,'p_statement','lexer.py',114),
  ('statement -> if_statement statement','statement',2,'p_statement','lexer.py',115),
  ('expression_statement -> assignment_statement SEMI','expression_statement',2,'p_expression_statement','lexer.py',121),
  ('expression_statement -> func_call SEMI','expression_statement',2,'p_expression_statement','lexer.py',122),
  ('expression_statement -> declarator SEMI','expression_statement',2,'p_expression_statement','lexer.py',123),
  ('assignment_statement -> ID EQUALS expression','assignment_statement',3,'p_assignment_statement','lexer.py',128),
  ('assignment_statement -> ID EQUALS func_call','assignment_statement',3,'p_assignment_statement','lexer.py',129),
  ('expression -> binary_expression','expression',1,'p_expression','lexer.py',134),
  ('expression -> cond_expression','expression',1,'p_expression','lexer.py',135),
  ('binary_expression -> unary_expression','binary_expression',1,'p_binary_expression','lexer.py',140),
  ('binary_expression -> ICONST PLUS binary_expression','binary_expression',3,'p_binary_expression','lexer.py',141),
  ('binary_expression -> ICONST MINUS binary_expression','binary_expression',3,'p_binary_expression','lexer.py',142),
  ('binary_expression -> ID PLUS binary_expression','binary_expression',3,'p_binary_expression','lexer.py',143),
  ('binary_expression -> ID MINUS binary_expression','binary_expression',3,'p_binary_expression','lexer.py',144),
  ('binary_expression -> LPAREN ICONST PLUS binary_expression RPAREN','binary_expression',5,'p_binary_expression','lexer.py',145),
  ('binary_expression -> LPAREN ICONST MINUS binary_expression RPAREN','binary_expression',5,'p_binary_expression','lexer.py',146),
  ('binary_expression -> LPAREN ID PLUS binary_expression RPAREN','binary_expression',5,'p_binary_expression','lexer.py',147),
  ('binary_expression -> LPAREN ID MINUS binary_expression RPAREN','binary_expression',5,'p_binary_expression','lexer.py',148),
  ('unary_expression -> ID','unary_expression',1,'p_unary_expression','lexer.py',154),
  ('unary_expression -> ICONST','unary_expression',1,'p_unary_expression','lexer.py',155),
  ('cond_expression -> unary_expression GT unary_expression','cond_expression',3,'p_cond_expression','lexer.py',160),
  ('cond_expression -> unary_expression LT unary_expression','cond_expression',3,'p_cond_expression','lexer.py',161),
  ('cond_expression -> unary_expression EQ unary_expression','cond_expression',3,'p_cond_expression','lexer.py',162),
  ('cond_expression -> cond_expression OR cond_expression','cond_expression',3,'p_cond_expression','lexer.py',163),
  ('cond_expression -> NOT cond_expression','cond_expression',2,'p_cond_expression','lexer.py',164),
  ('cond_expression -> LPAREN cond_expression OR cond_expression RPAREN','cond_expression',5,'p_cond_expression','lexer.py',165),
  ('cond_expression -> NOT LPAREN cond_expression RPAREN','cond_expression',4,'p_cond_expression','lexer.py',166),
  ('if_statement -> IF LPAREN cond_expression RPAREN LBRACE statement RBRACE','if_statement',7,'p_if_statement','lexer.py',172),
  ('func_call -> ID LPAREN arg_list RPAREN','func_call',4,'p_func_call','lexer.py',177),
  ('arg_list -> empty','arg_list',1,'p_arg_list_1','lexer.py',182),
  ('arg_list -> ID','arg_list',1,'p_arg_list_2','lexer.py',187),
  ('arg_list -> ICONST','arg_list',1,'p_arg_list_2','lexer.py',188),
  ('arg_list -> SCONST','arg_list',1,'p_arg_list_2','lexer.py',189),
  ('arg_list -> ID COMMA arg_list','arg_list',3,'p_arg_list_2','lexer.py',190),
  ('arg_list -> ICONST COMMA arg_list','arg_list',3,'p_arg_list_2','lexer.py',191),
  ('arg_list -> SCONST COMMA arg_list','arg_list',3,'p_arg_list_2','lexer.py',192),
  ('function_declaration -> func_decl SEMI','function_declaration',2,'p_function_declaration','lexer.py',197),
  ('func_decl -> TYPEID ID LPAREN param_list RPAREN','func_decl',5,'p_func_decl','lexer.py',203),
  ('declarator -> TYPEID ID','declarator',2,'p_declarator','lexer.py',209),
  ('param_list -> empty','param_list',1,'p_param_list_1','lexer.py',215),
  ('param_list -> declarator','param_list',1,'p_param_list_2','lexer.py',221),
  ('param_list -> declarator COMMA param_list','param_list',3,'p_param_list_2','lexer.py',222),
  ('empty -> <empty>','empty',0,'p_empty','lexer.py',227),
]
