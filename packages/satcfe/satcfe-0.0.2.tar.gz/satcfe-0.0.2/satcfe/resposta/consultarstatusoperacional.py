# -*- coding: utf-8 -*-
#
# satcfe/resposta/consultarstatusoperacional.py
#
# Copyright 2015 Base4 Sistemas Ltda ME
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import base64
import errno
import os
import tempfile

from satcomum.util import forcar_unicode

from ..excecoes import ExcecaoRespostaSAT
from ..util import a2date
from ..util import a2datetime
from ..util import normalizar_ip
from .padrao import RespostaSAT
from .padrao import analisar_retorno


DESBLOQUEADO = 0
BLOQUEADO_SEFAZ = 1
BLOQUEADO_CONTRIBUINTE = 2
BLOQUEADO_AUTO = 3
BLOQUEADO_PARA_DESATIVACAO = 4

ESTADOS_OPERACAO = (
        (DESBLOQUEADO, u'Desbloqueado'),
        (BLOQUEADO_SEFAZ, u'Bloqueado pelo SEFAZ'),
        (BLOQUEADO_CONTRIBUINTE, u'Bloqueado pelo contribuinte'),
        (BLOQUEADO_AUTO, u'Bloqueado autonomamente'),
        (BLOQUEADO_PARA_DESATIVACAO, u'Bloqueado para desativação'),
    )


class RespostaConsultarStatusOperacional(RespostaSAT):
    """
    ER SAT, item 6.1.7. Consulta do status operacional do equipamento SAT.
    """

    @property
    def status(self):
        for valor, rotulo in ESTADOS_OPERACAO:
            if self.ESTADO_OPERACAO == valor:
                return rotulo
        return u'(desconhecido: {})'.format(self.ESTADO_OPERACAO)


    @staticmethod
    def analisar(retorno):
        resposta = analisar_retorno(forcar_unicode(retorno),
                funcao='ConsultarStatusOperacional',
                classe_resposta=RespostaConsultarStatusOperacional,
                campos=RespostaSAT.CAMPOS + (
                        ('NSERIE', unicode),
                        ('TIPO_LAN', unicode),
                        ('LAN_IP', normalizar_ip),
                        ('LAN_MAC', unicode),
                        ('LAN_MASK', normalizar_ip),
                        ('LAN_GW', normalizar_ip),
                        ('LAN_DNS_1', normalizar_ip),
                        ('LAN_DNS_2', normalizar_ip),
                        ('STATUS_LAN', unicode),
                        ('NIVEL_BATERIA', unicode),
                        ('MT_TOTAL', unicode), # int ?
                        ('MT_USADA', unicode), # int ?
                        ('DH_ATUAL', a2datetime),
                        ('VER_SB', unicode),
                        ('VER_LAYOUT', unicode),
                        ('ULTIMO_CF_E_SAT', unicode),
                        ('LISTA_INICIAL', unicode),
                        ('LISTA_FINAL', unicode),
                        ('DH_CFE', a2datetime),
                        ('DH_ULTIMA', a2datetime),
                        ('CERT_EMISSAO', a2date),
                        ('CERT_VENCIMENTO', a2date),
                        ('ESTADO_OPERACAO', int),
                    )
            )
        if resposta.EEEEE not in ('10000',):
            raise ExcecaoRespostaSAT(resposta)
        return resposta
