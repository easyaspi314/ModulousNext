from flask import Blueprint, render_template, abort
from SpaceDock.objects import User, BlogPost, Game, GameVersion
from SpaceDock.database import db
from SpaceDock.common import *
from SpaceDock.config import _cfg
from sqlalchemy import desc

import_gb = Blueprint('import_gb', __name__, template_folder='../../templates/import_gb')

@import_gb.route("/import_gb")
def import_monkeys():
    games = Game.query.filter(Game.active == True).order_by(desc(Game.id)).all()
    if session.get('gameid'):
        if session['gameid']:
            ga = Game.query.filter(Game.id == session['gameid']).order_by(desc(Game.id)).first()
        else:
            ga = Game.query.filter(Game.short == 'melee').order_by(desc(Game.id)).first()
    else:
        ga = Game.query.filter(Game.id == 1).order_by(desc(Game.id)).first()
    session['game'] = ga.id;
    session['gamename'] = ga.name;
    session['gameshort'] = ga.short;
    session['gameid'] = ga.id;
    game_versions = GameVersion.query.filter(GameVersion.game_id == ga.id).order_by(desc(GameVersion.id)).all()
    return render_template("import.html", game_versions=game_versions,game=games,ga=ga)
