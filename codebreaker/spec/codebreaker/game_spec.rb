require 'spec_helper'

module Codebreaker
  describe Game do             

    let(:output) { output = double("output").as_null_object }

    let(:game) { game = Game.new(output) }

    describe ".start" do      
      it "sends the welcome message" do        
        output.should_receive(:puts).with("welcome to codebreaker")
        game.start
      end

      it "sends the submit guess prompt" do
        output.should_receive(:puts).with("submit a guess:")        
        game.start
      end
    end

    describe ".guess" do
      context "no matches" do
        it "sends an empty mark" do
          output.should_receive(:puts).with("")        
          game.start('1234')
          game.guess('6666')
        end
      end

      context "1 exact match" do
        it "sends a mark with '+'" do
          output.should_receive(:puts).with("+")        
          game.start('1234')
          game.guess('1666')
        end
      end

      context "1 number match" do
        it "sends a mark with '-'" do
          output.should_receive(:puts).with("-")        
          game.start('1234')
          game.guess('2666')
        end
      end

      context "1 exact match 1 number match" do
        it "sends a mark with '+-'" do
          output.should_receive(:puts).with("+-")        
          game.start('1234')
          game.guess('1366')
        end
      end

      context "1 number match 1 exact match, in that order" do
        it "sends a mark with '+-'" do
          output.should_receive(:puts).with("+-")        
          game.start('1234')
          game.guess('3266')
        end
      end

      context "duplicated matches" do
        it "sends a mark with '+'" do
          output.should_receive(:puts).with("+")        
          game.start('1234')
          game.guess('1111')
        end
      end
    end
  end
end
